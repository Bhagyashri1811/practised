# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:59:20 2021

@author: Bhagyashri
"""
"""
Problem 3
(A) Suppose we have to take any strings from user. Identify whether information present in the string is
• Collection of characters
• Collection of Special characters
• Collection of Numerical data
"""

string = input("Enter ths string: ")
if string.isalnum():
    print(f"The given string {string} is Character")
elif string.isdigit():
    print(f"The given string {string} is numeric")
else:
     print(f"The given string {string} is Special character")

