# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:05:17 2023

@author: kavita narayan
"""

#5. Write a Python function that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

print("\nWelcome to my Program")
items = [n for n in input("Enter the elements : ").split('-')]
items.sort()
print("\nSorted elements : ")
print('-'.join(items))