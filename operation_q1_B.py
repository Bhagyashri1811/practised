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

def And(a,b):
    c=a and b
    print(f"{a} & {b} is {c}")

def Or(a,b):
    c=a or b
    print(f"{a} | {b} is {c}")

def less_than(a,b):
    c=a < b
    print(f"{a} << {b} is {c}")

def greater_than(a,b):
    c=a > b
    print(f"{a} >> {b} is {c}")
    
def exp(a,b):
    c= not b
    print(f" ~{b} is {c}")
    print(f" ~{a} is {not a}")
    
And(fint,sint)
And(ffloat,sfloat)
And(fstr,sstr)
And(fdoub,sdoub)

Or(fint,sint)
Or(ffloat,sfloat)
Or(fstr,sstr)
Or(fdoub,sdoub)

less_than(fint,sint)
less_than(ffloat,sfloat)
less_than(fstr,sstr)
less_than(fdoub,sdoub)

greater_than(fint,sint)
greater_than(ffloat,sfloat)
greater_than(fstr,sstr)
greater_than(fdoub,sdoub)

exp(fint,sint)
exp(ffloat,sfloat)
exp(fstr,sstr)
exp(fdoub,sdoub)
