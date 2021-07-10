# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:41:39 2021

@author: Bhagyashri
"""

def linearsearch(key,ar):
    for i in range(0,len(ar)):
        if(ar[i]==key):
            return i
        
    
    
ar=[1,2,8,10,4,6,3,9,5]
key=5
status=linearsearch(key, ar)
print("Element founded at",status)