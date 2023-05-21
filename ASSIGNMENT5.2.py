# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:23:55 2023

@author: kavita narayan
"""

#2.Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range and the number)

#The number and range provided by user.
n=int(input("Enter the number: "))
x=int(input("Enter the range: "))
print("The numbers divisible are: ")
for i in range(x):
    if i%n==0:
        print(i) #divisible number
        