# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:48:56 2019

@author: Meg_94
"""

f = open("rosalind_ini2.txt","r")
raw_lines = f.readlines()

nums = raw_lines[0].rstrip("\n").split(' ')

a = int(nums[0])
b = int(nums[1])

c = a**2 + b**2

print c