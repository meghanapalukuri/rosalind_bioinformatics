# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:05:34 2019

@author: Meg_94
"""

fnm = "rna.txt"
fnm = "test.txt"
fnm = "rosalind_prot.txt"

with open(fnm) as f:
    line = f.readline().rstrip("\r\n")

rna_codon_csv = ["UUU","F","CUU","L","AUU","I","GUU","V",
"UUC","F","CUC","L","AUC","I","GUC","V",
"UUA","L","CUA","L","AUA","I","GUA","V",
"UUG","L","CUG","L","AUG","M","GUG","V",
"UCU","S","CCU","P","ACU","T","GCU","A",
"UCC","S","CCC","P","ACC","T","GCC","A",
"UCA","S","CCA","P","ACA","T","GCA","A",
"UCG","S","CCG","P","ACG","T","GCG","A",
"UAU","Y","CAU","H","AAU","N","GAU","D",
"UAC","Y","CAC","H","AAC","N","GAC","D",
"UAA","Stop","CAA","Q","AAA","K","GAA","E",
"UAG","Stop","CAG","Q","AAG","K","GAG","E",
"UGU","C","CGU","R","AGU","S","GGU","G",
"UGC","C","CGC","R","AGC","S","GGC","G",
"UGA","Stop","CGA","R","AGA","R","GGA","G",
"UGG","W","CGG","R","AGG","R","GGG","G"]

keys = rna_codon_csv[0::2]
vals = rna_codon_csv[1::2]

rna_codon_dict = dict(zip(keys,vals))

# Extract mRNA portion that translates a protein 

# Search for start codon - AUG 
start_ind = line.find("AUG")

line_start = line[start_ind:]

pres_codon = "AUG"

codon_start_ind = 3
prot = []
while pres_codon not in ["UAA","UAG","UGA"]:
    prot.append(rna_codon_dict[pres_codon])
    pres_codon = line_start[codon_start_ind:codon_start_ind+3]
    codon_start_ind = codon_start_ind + 3

protein = ''.join(prot)

with open("sol.txt","w") as f_sol:
    f_sol.write(protein)
