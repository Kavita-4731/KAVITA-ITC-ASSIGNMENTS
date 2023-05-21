# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:07:04 2023

@author: kavita narayan
"""

#9. Write a program to count the number of occurrences of each word in the list(List entered by the user).

l=[]
n=int(input("\nlength of list: ")) #number of desired elements
for i in range(n):
    a=input("Enter value: ") #appending list
    l.append(a)


for i in l:
    count=0
    for ele in l:
        if (ele == i):
            count = count + 1
    print("Count of",i,"=",count) #count of each word