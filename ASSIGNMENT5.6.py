# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:02:13 2023

@author: kavita narayan
"""

#6.Write a python program to print the prime numbers for a user input range.
# User will enter range  
lower= int(input("Please, Enter the Lowest Range Value: "))  
upper= int(input("Please, Enter the Upper Range Value: "))  
  
print("The Prime Numbers in the range are: ")  
for number in range (lower, upper + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  #breaks if divisible by another number except 1 and itself.
        else:  
            print (number)
