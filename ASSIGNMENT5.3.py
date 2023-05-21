# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:25:26 2023

@author: kavita narayan
"""

#3.Program to calculate the area of a triangle using heron’s formula. 

# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))

if a<b+c:
    if c<a+b:
        if b<a+c:
            # calculate the semi-perimeter  
            s = (a + b + c) / 2  
  
            # calculate the area  
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
            print('The area of the triangle is ',area)
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("invalid input")
