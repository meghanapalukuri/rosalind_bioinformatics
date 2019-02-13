# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:13:34 2019

@author: Meg_94
"""

f = open("rosalind_ini4.txt","r")
raw_lines = f.readlines()
nums = raw_lines[0].rstrip("\n").split(' ')

nums = [int(elt) for elt in nums]

a = nums[0]
b = nums[1]


if(a % 2 != 0): # If a is odd 
    start = a
else:
    start = a + 1

if(b % 2 != 0): # If b is odd 
    stop = b + 1
else:
    stop = b
    
odd_nums = range(start,stop,2)
    
print(sum(odd_nums))