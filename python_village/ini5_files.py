# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:30:22 2019

@author: Meg_94
"""

f = open("rosalind_ini5.txt","r")
raw_lines = f.readlines()

n_lines = len(raw_lines)

odd_line_inds = range(1,n_lines,2)
odd_lines = [raw_lines[i] for i in odd_line_inds]

f.close()

f_out = open("rosalind_ini5_sol.txt","w")
for line in odd_lines:
    f_out.write(line)
f_out.close()