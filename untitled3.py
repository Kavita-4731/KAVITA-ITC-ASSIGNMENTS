# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 07:44:07 2023

@author: Hullash
"""

a = int(input("Gross Income: "))
b = int(input("No of Dependents: "))
taxable_income = a -10000 -3000*b
tax = taxable_income*0.2

if(taxable_income<0):
    print("Tax: 0")
else:
    print("Tax: ", tax)
    
