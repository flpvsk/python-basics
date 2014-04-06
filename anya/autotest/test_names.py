'''
Created on Apr, 06

@author: arakann
'''

import os
import re


def unique(lst):
    output = {i : None for i in lst}
    return output.keys()



logs_dir = "C:\\test-results\\"
test_names_lst=[]
test_names_lst_unique = []
#for f in logs_dir:
files_lst = os.listdir(logs_dir)
for f in  files_lst:
    f = open(logs_dir + f, 'r')
    file_content = f.read().split(';')
    for el in file_content:
        try:
            match = re.search(r'\'[\w,\d]*\'', el)
            test_names_lst.append(match.group())
        except:
            pass
print unique(test_names_lst)