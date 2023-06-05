# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:32:05 2023

@author: kavita narayan
"""

#2. Write a Python function that checks whether a passed string is palindrome or not.

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
