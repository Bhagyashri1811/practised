# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:15:33 2021

@author: Bhagyashri
"""

#Karatsuba Algorithm

x=int(input("Enter Number 1: "))
y=int(input("Enter Number 2: "))

def karatsuba(x,y):
    #base case
    if x<10 or y<10:
        return x*y
    m=max(len(str(x)) ,len(str(y)))
    
    if m%2!=0:
        m-=1 #converting odd number to even
    a,b=divmod(x, 10**int(m/2))
    c,d=divmod(y, 10**int(m/2))
    ac=karatsuba(a, c)
    bd=karatsuba(b, d)
    ad_bc=karatsuba((a+b), (c+d))-ac-bd
    
    return ((ac*(10**m))+((ad_bc)*(10**int(m/2)))+bd) #karatsuba Equation




s=karatsuba(x,y)
print(s)