# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:03:25 2023

@author: kavita narayan
"""

#Q4 Write a Python function to check whether a string is a pangram or not.

print("\nWelcome to my Program")
def ispangram(string):
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in alph :
        if i not in string.lower():
            return False
    return True
string = input("\nEnter a string : ")
print(ispangram(string))