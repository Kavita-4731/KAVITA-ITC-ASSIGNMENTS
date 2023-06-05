# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:16:11 2023

@author: kavita narayan
"""

#9. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].

print("\nWelcome to my Program")
class solution:
    def validity(self,str1):
        accumulate=[]
        parentheses={"(":")","[":"]","{":"}"}
        for i in str1 :
            if i in parentheses:
                accumulate.append(i)
            elif len(accumulate)==0 or parentheses[accumulate.pop()]!=i:
                return False
        return len(accumulate)==0
print(solution().validity("[)"))