# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:05:39 2023

@author: kavita narayan
"""

#Input 10 integer values from the user. Write a python program to find and print the following:

#a. positive numbers
print("\nAns8")            
l=[]
for i in range(10):
    a=int(input("Enter value: "))
    l.append(a)
print("positive numbers")
for i in l:
    if i>0:
        print(i)
#b. negative numbers
print("negative numbers")
for i in l:
    if i<0:
        print(i)
#c. odd numbers
print("odd numbers")
for i in l:
    if i%2==1:
        print(i)
#d. even numbers
print("even numbers")
for i in l:
    if i%2==0:
        print(i)
#e. Number of times each number occurs in the List
print("Number of times each number occurs in the List")
for i in l:
    count=0
    for ele in l:
        if (ele == i):
            count = count + 1
    print("Count of",i,"=",count)