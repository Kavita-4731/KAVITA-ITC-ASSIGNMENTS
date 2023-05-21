# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:04:06 2023

@author: kavita narayan
"""

#7. python program to find the numbers which are multiple of 7 and divisible by 11 in the range 1-500.
for i in range(1,500):
    if i%7==0:
        if i%11==0:
            print(i)