# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:23:57 2019

@author: Meg_94
"""

#fnm = "rosalind_dna.txt"
fnm = "rosalind_rna.txt"

with open(fnm,"r") as f:
    raw_lines = f.readlines()
    
first_line = raw_lines[0].rstrip("\r\n")

rna=first_line.replace("T","U")

with open("sol.txt","w") as f_sol:
    f_sol.write(rna)
    
