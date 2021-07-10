# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:00:08 2021

@author: Bhagyashri
"""

#PROBLEM 2:::
tmp = float(input("enter temperature"))
if(tmp<=0):
    print("It is freezing")
elif(tmp<15):
    print("It is cold")
elif(tmp<25):
    print("It is a nice day")
else:
    print("It is hot!")