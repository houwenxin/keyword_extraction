# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:45:53 2019

@author: houwenxin
"""

class evaluation:
    def __init__(self, precision=0.0, recall=0.0, f1=0.0):
        self.f1 = f1
        self.precision = precision
        self.recall = recall
    
    def evaluate(self, true_keywords, pred_keywords):
        matched = 0
        num_pred = 0
        for pred_keyword in pred_keywords:
            num_pred += 1
            #print(pred_keyword)
            if pred_keyword in true_keywords:
                matched += 1
        recall = matched * 1.0 / len(true_keywords)
        precision = matched * 1.0 / num_pred
        if matched == 0:
            f1 = 0.0
        else:
            f1 = 2 * recall * precision / (recall + precision)
        self.f1 += f1
        self.precision += precision
        self.recall += recall
    
    def report(self, document_num):
        f1 = self.f1 / document_num
        precision = self.precision / document_num
        recall = self.recall / document_num
        print("Document Number: ", document_num)
        print("Precision: ", precision)
        print("Recall: ", recall)
        print("F1 Score: ", f1)
    
    def evaluate_from_result_file(self, file_path):
        doc_num = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                doc_num += 1
                true_keywords = line.split(",")[0].strip("\n").split(":")
                pred_keywords = line.split(",")[1].strip("\n").split(":")
                self.evaluate(true_keywords, pred_keywords)
        self.report(doc_num)

if __name__ == "__main__":
    result_file_path = "result/tfidf_true_pred_pairs.txt"
    evaluator = evaluation()
    evaluator.evaluate_from_result_file(result_file_path)