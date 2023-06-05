# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:00:46 2023

@author: kavita narayan
"""

#3. Write a Python function that prints out the first n rows of Pascal's triangle.
print("\nWelcome to my Program")
from math import factorial
def pascaltriangle(numRows):
    for i in range(numRows):
        for j in range(numRows - i + 1):
            print(end = " ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end = " ")

        print("\n")
pascaltriangle(5)