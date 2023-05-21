# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:10:40 2023

@author: kavita narayan
"""

# Q5) Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
# Example: Input the number of rows = 5, then the pattern should come out as given below.
# If the count of the alphabet gets exhausted, repeat the alphabet from A.

n = int(input("number of rows: "))
asciichr = 65
# outer loop for ith rows
for i in range(0, n):
    # inner loop for jth columns
    for j in range(0, i+1):
        char = chr(asciichr)
        print(char, end="")
        asciichr += 1
    print()
    


