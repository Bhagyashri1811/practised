# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:50:22 2021

@author: Bhagyashri
"""
"""
Take two integer, two float, two double, two character from user and Perform (A) Sum, product, division, modulous and substraction. (B) All biwise operator & | ~ ^ << >>
"""
fint= int(input("Enter the first integer number: "))
sint= int(input("Enter the second integer number: "))

ffloat= float(input("Enter the first float number: "))
sfloat= float(input("Enter the second float number: "))

fdoub= eval(input("Enter the first double number: "))
sdoub= eval(input("Enter the second double number: "))

fstr= ascii(input("Enter the first character: "))
sstr= ascii(input("Enter the first character: "))
print(fstr)

def Add(a,b):
    c=a+b
    print(f"Addition of {a} + {b} is {c}")

def Sub(a,b):
    c=a-b
    print(f"Subtraction of {a} - {b} is {c}")

def Mul(a,b):
    c=a*b
    print(f"Multiplication of {a} * {b} is {c}")

def Div(a,b):
    c=a/b
    print(f"Division of {a} / {b} is {c}")
    
def Mod(a,b):
    c=a%b
    print(f"Modulo of {a} % {b} is {c}")
    
Add(fint,sint)
Add(ffloat,sfloat)
Add(fstr,sstr)
Add(fdoub,sdoub)

Sub(fint,sint)
Sub(ffloat,sfloat)
Sub(fdoub,sdoub)

Mul(fint,sint)
Mul(ffloat,sfloat)
Mul(fdoub,sdoub)

Div(fint,sint)
Div(ffloat,sfloat)
Div(fdoub,sdoub)

Mod(fint,sint)
Mod(ffloat,sfloat)
Mod(fdoub,sdoub)
