# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 19:56:15 2019

@author: houwenxin
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import utils
from sklearn.externals import joblib
import numpy as np

def TFIDF_keyword_extraction(documents, stopwords, extract_num=1):
    all_documents = []
    seg = utils.segmentor()
    for document in documents:
        document = list(seg.segment(document)) 
        all_documents.append(" ".join(document))
    
    del seg, documents
    
    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", max_df=0.75, stop_words=stopwords)
    model = vectorizer.fit(all_documents)
    joblib.dump(model, "model/tfidf_model.model")
    tfidf = model.transform(all_documents)
    tfidf_array = tfidf.toarray()
    print("TF-IDF Data Matrix Size: ", tfidf_array.shape)
    
    del all_documents, stopwords, tfidf, model # 释放没用的内存
    
    dictionary = dict(zip(vectorizer.vocabulary_.values(), vectorizer.vocabulary_.keys()))
    keywords = []
    for row in range(tfidf_array.shape[0]):
        keyword = []
        idxs = np.argsort(tfidf_array[row])[::-1][:extract_num]
        for idx in idxs:
            keyword.append(dictionary[idx])
        keywords.append(keyword)
        
    del tfidf_array, dictionary, keyword # 继续释放没用的内存
    
    print("Keywords are successfully extracted.")
    return keywords

def write_result_to(file_path, true_keywords, pred_keywords):
    print("Writing true and predicted keywords to file {}...".format(file_path))
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(len(true_keywords)):
            true_keyword = utils.list_to_str(true_keywords[i]).lower() # 把labels中的英文字母全部换成小写
            pred_keyword = utils.list_to_str(pred_keywords[i])
            pairs = true_keyword + "," + pred_keyword + "\n"
            file.write(pairs)
    print("Done.")

if __name__ == "__main__":
    full_data_path = "data/full_data.txt"
    stop_word_path = "lib/chinese_stop_word_more.txt"

    documents, true_keywords = utils.load_data(full_data_path)
    stopwords = utils.load_stop_word(stop_word_path)
    pred_keywords = TFIDF_keyword_extraction(documents, stopwords, extract_num=3)
    del stopwords, documents #   继续释放内存
    result_file_path = "result/tfidf_true_pred_pairs.txt"
    write_result_to(result_file_path, true_keywords, pred_keywords)
    
    
    