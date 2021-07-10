# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:17:59 2021

@author: Bhagyashri
"""

age = int(input("Enter you age in year in number: "))
agem =int(input("Enter you age in months in number: "))
gender = input("Enter your gender: ")

if age < 18 or agem < 11:
    print("Sorry you are not eligible for license")
else:
    print("You are eligible for license")
    
