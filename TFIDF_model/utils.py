# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 18:55:06 2019

Some utils functions, e.g. load and pre-process fulldata.txt for keyphrase extraction.

Data Type = ID € TITLE € CONTENT € TAGS
 
@author: houwenxin
"""

import pyltp
import jieba

default_segmentor = "pyltp"
cws_model_path = "D:\\Study\\Nanjing_University\\Thesis\\ltp_data_v3.4.0\\cws.model"

class segmentor:
    def __init__(self, segmentor=default_segmentor):
        self.segmentor = segmentor
        if self.segmentor == "pyltp":
            self.ltp_segmentor = pyltp.Segmentor()
            self.ltp_segmentor.load(cws_model_path)
    def segment(self,sentence):
        if self.segmentor == "jieba":
            sentence_words = list(jieba.cut(sentence, cut_all=False))
        elif self.segmentor == "pyltp":
            sentence_words = list(self.ltp_segmentor.segment(sentence))
        return sentence_words
    def __del__(self):
        if self.segmentor == "pyltp":
            self.ltp_segmentor.release()            

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

def load_stop_word(file_path):
    stopwords = [line.strip() for line in open(file_path, "r", encoding="utf-8").readlines()]
    print("Stop words loaded from \'{}\'".format(file_path))
    return stopwords

def list_to_str(lst):
    string = "" + lst[0]
    for i in range(1, len(lst)):
        string += ":"
        string += lst[i]
    return string
        
def test(full_data_path):
    documents, labels = load_data(full_data_path)
    print(documents[0])
    print(labels[0])