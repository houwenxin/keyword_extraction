# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:25:03 2019

问题：
1. 如果文章内容太长了怎么办？

@author: houwenxin
"""

import utils

def analysis(documents, labels):
    absent_keywords = 0
    present_keywords = 0
    avg_doc_len = 0.0
    max_doc_len = 0
    min_doc_len = 8000
    seg = utils.segmentor()    
    for i in range(len(documents)):
        document_words = seg.segment(documents[i])
        doc_len = len(document_words)
        avg_doc_len += doc_len
        if doc_len > max_doc_len:
            max_doc_len = doc_len
            print("Larger length of document: {}, length: {} ".format(i, doc_len))
        if doc_len < min_doc_len:
            min_doc_len = doc_len
        keywords = labels[i]
        for keyword in keywords:
            if keyword in document_words:
                present_keywords += 1
            else:
                absent_keywords += 1
    del seg
    total = present_keywords + absent_keywords
    print("Number of present keywords: {}, percent: {}".format(present_keywords, 1.0 * present_keywords / total))
    print("Number of absent keywords: {}, percent: {}".format(absent_keywords, 1.0 * absent_keywords / total))
    print("Average length of documents: ", avg_doc_len / len(documents))
    print("Largest length of documents: ", max_doc_len)
    print("Smallest length of documents: ", min_doc_len)

if __name__ == "__main__":
    stop_word_path = "lib/chinese_stop_word_more.txt"
    full_data_path = "data/full_data.txt"
    documents, labels = utils.load_data(full_data_path)
    #stopwords = utils.load_stop_word(stop_word_path)
    analysis(documents, labels)
    del stopwords, documents, labels