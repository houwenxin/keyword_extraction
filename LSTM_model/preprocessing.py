# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 15:25:03 2019

Used for pre-processing.

@author: houwenxin
"""

import utils

def convert_to_pair(src_file_path, dest_file_path):
    documents, keywords = utils.load_data(src_file_path)
    