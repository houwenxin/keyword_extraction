# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:55:06 2019

Some utils functions, e.g. load and pre-process fulldata.txt for keyphrase extraction.

Data Type = ID € TITLE € CONTENT € TAGS
 
@author: houwenxin
"""

full_data_path = "./full_data.txt"

def load_data(file_path, max_tag_num = 100):
    documents = []
    labels = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            #line = file.readline()
            tags = line.split("€")[3].replace("\n", "")
            tags = tags.split(",")
            tags = list(tags)
            if len(tags) < max_tag_num:
                data = line.split("€")[1] + line.split("€")[2]
                #if(tags[0] == ""): continue # 去除实际为空的tag
                documents.append(data)
                #labels.append(tags)
                labels.append(tags)
    print("Data Size: ", len(documents))
    return documents, labels

def list_to_str(lst):
    string = "" + lst[0]
    for i in range(1, len(lst)):
        string += ":"
        string += lst[i]
    return string
        
def test():
    documents, labels = load_data(full_data_path)
    print(documents[0])
    print(labels[0])