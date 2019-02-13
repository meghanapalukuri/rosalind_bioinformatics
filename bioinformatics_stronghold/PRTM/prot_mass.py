# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:45:46 2019

@author: Meg_94
"""
fnm = "input.txt"
fnm = "rosalind_prtm.txt"
with open(fnm) as f:
    line = f.readline().rstrip("\r\n")
    
aa_wts_csv = ["A",71.03711,
"C",103.00919,
"D",115.02694,
"E",129.04259,
"F",147.06841,
"G",57.02146,
"H",137.05891,
"I",113.08406,
"K",128.09496,
"L",113.08406,
"M",131.04049,
"N",114.04293,
"P",97.05276,
"Q",128.05858,
"R",156.10111,
"S",87.03203,
"T",101.04768,
"V",99.06841,
"W",186.07931,
"Y",163.06333]

keys = aa_wts_csv[0::2]
vals = aa_wts_csv[1::2]
aa_wts_dict = dict(zip(keys,vals))

prot_aa_wts = [aa_wts_dict[aa] for aa in line]

prot_wt = sum(prot_aa_wts)
print prot_wt
    

