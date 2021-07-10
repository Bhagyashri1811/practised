# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:37:11 2021

@author: Bhagyashri
"""
"""
Problem 1: Suppose we have to take following data from user: 23 67890 45.67 56.78906543 ‘&’ “ROBOT 2.0” 8141719227. Once the data is taken then it also has to display at output screen with newline.

"""
n =int(input("How many inputs to be entered:"))
A= []

for b in range(0,n):

    k=input()
    if(k.isdigit()):
        k = int(k)
    elif(k.isalpha()):
        k=str(k)
    elif(k.replace('.', '', 1).isdigit() ==True):
        k = float(k)    
    A.append(k)
    
print(A)
for c in range(0,n):
    print(A[c])
