# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 22:25:03 2019

@author: houwenxin
"""

import utils
import jieba

def analysis(documents, labels):
    absent_keywords = 0
    present_keywords = 0
    for i in range(len(documents)):
        document_words = list(jieba.cut(documents[i], cut_all=False))
        keywords = labels[i]
        for keyword in keywords:
            if keyword in document_words:
                present_keywords += 1
            else:
                absent_keywords += 1
    total = present_keywords + absent_keywords
    print("Number of present keywords: {}, percent: {}".format(present_keywords, 1.0 * present_keywords / total))
    print("Number of absent keywords: {}, percent: {}".format(absent_keywords, 1.0 * absent_keywords / total))

if __name__ == "__main__":
    full_data_path = "data/full_data.txt"
    documents, labels = utils.load_data(full_data_path)
    analysis(documents, labels)