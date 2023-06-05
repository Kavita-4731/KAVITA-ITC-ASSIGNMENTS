# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:12:36 2023

@author: kavita narayan
"""

#6. Write a Python function student_data () which will print the id of a student (student_id).

print("\nWelcome to my Program")
def student_data(student_id, **kwargs):
    print("\nStudent ID:", student_id)
    if "student_name" in kwargs:
        print("Student Name :", kwargs['student_name'])
    if "student_name" and "student_class" in kwargs:
        print("Student Name :", kwargs['student_name'])
        print("Student Class :", kwargs['student_class'])

student_data(student_id = '21102132', student_name = 'KAVITA NARAYAN')

student_data(student_id='21102132', student_name='KAVITA NARAYAN', student_class='XII')
