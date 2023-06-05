# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:23:45 2023

@author: kavita narayan
"""

#7.Write a Python program to create two empty classes, Student and Marks.

print("\nWelcome to my Program")
class Student:
    pass
class Marks:
    pass
Kavita=Student()
a_grade=Marks()
print("To check whether they are instances of said classes or not:")
print(isinstance(Kavita,Student))
print(isinstance(Kavita,Marks))
print(isinstance(a_grade,Marks))
print(isinstance(a_grade,Student))
print("\nTo check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(Student,object))
print(issubclass(Marks,object))
