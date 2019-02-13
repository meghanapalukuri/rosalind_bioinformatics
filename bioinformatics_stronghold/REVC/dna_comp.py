# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:37:43 2019

@author: Meg_94
"""

#fnm= "dna.txt"
fnm= "rosalind_revc.txt"

with open(fnm,"r") as f:
    raw_line = f.readline()
    
line = raw_line.rstrip("\r\n")

rev_str = line[::-1]

keys = ['A','T','G','C']
vals = ['T','A','C','G']
comps = dict(zip(keys,vals))

comp_dna_lts = [comps[char] for char in rev_str]
comp_dna = ''.join(comp_dna_lts)

with open("sol.txt","w") as f_sol:
    f_sol.write(comp_dna)