# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:27:03 2023

@author: kavita narayan
"""

# 4.Write a Python program to construct the following pattern, using a nested for loop.

n=5; 
for i in range(n):
    for j in range(i):
        print ('* ', end="") 
    print('') #to change line

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('') #to change line
    