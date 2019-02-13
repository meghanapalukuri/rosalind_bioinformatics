# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:39:56 2019

@author: Meg_94
"""

f = open("Ecoli_genome.txt","r")
#f = open("rosalind_dna.txt","r")
lines = f.readlines()
f.close()

lines = [line.rstrip("\r\n") for line in lines]

single_line = ''.join(lines)

nucleotide = {}

for nuc in single_line:
    if nucleotide.has_key(nuc):
        nucleotide[nuc] += 1
    else:
        nucleotide[nuc] = 1
        
#print nucleotide["A"]," ",nucleotide["C"]," ",nucleotide["G"]," ",nucleotide["T"]

nuc_interest = ["A","C","G","T"]
counts = [nucleotide[n] for n in nuc_interest]
tot_ATGC = float(sum(counts))
percs = [100*counts[i]/tot_ATGC for i in range(len(nuc_interest)) ]

for i in range(len(nuc_interest)):
    print "Nucleotide {0} occurs {1} times or {2} %".format(nuc_interest[i], counts[i], percs[i])
