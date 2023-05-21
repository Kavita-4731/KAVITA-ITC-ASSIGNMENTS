# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:07:40 2023

@author: kavita narayan
"""

#1.Program to reverse the string.

string = input("Enter string: ") #  string variable  
print("The original string  is : ",string)   
reverse_string = ""  # empty String  
count = len(string) # Find length of a string and save in count variable  
while count > 0:   
    reverse_string += string[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print("The reversed string using a while loop is : ",reverse_string)