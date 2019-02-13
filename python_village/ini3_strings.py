# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:01:02 2019

@author: Meg_94
"""

f = open("rosalind_ini3.txt","r")
raw_lines = f.readlines()

s = raw_lines[0].rstrip("\n")
nums = raw_lines[1].rstrip("\n").split(' ')

nums = [int(elt) for elt in nums]
sol = s[nums[0]:nums[1]+1] + ' ' + s[nums[2]:nums[3]+1]

print(sol)