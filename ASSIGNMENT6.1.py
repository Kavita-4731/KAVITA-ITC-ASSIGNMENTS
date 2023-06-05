# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:22:02 2023

@author: kavita narayan
"""

#1. Write a Python function to check whether a number is perfect or not.
print("\nWelcome to my Program")
def isperfectnum(n):
    sum = 0
    sum_all = 0
    for i in range (1,n):
        if n % i == 0:
            sum += i
            sum_all += i
    sum2 = (sum_all+n)//2
    return sum == n , sum2 == n
m = int(input())
print(isperfectnum(m))