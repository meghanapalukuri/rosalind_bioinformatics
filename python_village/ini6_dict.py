# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 11:57:26 2019

@author: Meg_94
"""

fname = "rosalind_ini6.txt"
#fname="input.txt" 
with open(fname,"r") as f: # with automatically closes the file ! 
    raw_line = f.readlines()

first_line = raw_line[0].rstrip("\r\n")

words = first_line.split(' ')

count_words = {}
for word in words:
    if word in count_words:    
        count_words[word] +=1 
    else:
        count_words[word] = 1

with open("sol.txt","w") as f_sol:
    for key,val in count_words.items():
        f_sol.write(key+' '+str(val))
        f_sol.write("\n")