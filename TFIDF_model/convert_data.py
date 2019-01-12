# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:11:20 2019.

Convert NetEaseNewsKeyWordPost.dat to needed format for keyword extraction.

@author: houwenxin
    
Input dataType=KeywordPost : {
	"date": "news date",
	"summary":"news summary",
	"source":"news source",
	"id":"document id",
	"content":"document content",
	"title":"news title",
	"resourceKey":"",
	"extras":"",
	"userId":"",
	"tags":["tag1","tag2","tag3"]
}  //(Focus on news)

Output Data Type = ID € TITLE € CONTENT € TAGS
"""
import json
from html.parser import HTMLParser

src_file_path = "../data/NetEaseNewsKeywordPost.dat"
dest_file_path = "full_data.txt"

def convert_data(file_path):
    full_data = []
    html_parser = HTMLParser()
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            temp_data = json.loads(line)
            # €: alt + 0128
            data = temp_data["id"] + "€" + temp_data["title"] + "€" + \
                        temp_data["content"].replace("\n", "") + "€" + \
                        str(temp_data["tags"]).strip("[").strip("]").replace("'","").replace(" ", "")
            data = html_parser.unescape(data).replace("\n","") # 为了将爬虫中HTML语言的的转义字符，如&amp, &lt, &gt等转回正常的符号。
            full_data.append(data)
    print("Successfully convert data!")
    print("Full Data Size: ", len(full_data))
    return full_data

def write_full_data(file_path, full_data):
    with open(file_path, "w", encoding="utf-8") as file:
        for line in full_data:
            file.write(line)
            file.write("\n")
    print("Processed full data successfully written to {}.".format(dest_file_path))

if __name__ == "__main__":
    full_data = convert_data(src_file_path)
    write_full_data(dest_file_path, full_data)
