# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:35:45 2021

@author: Bhagyashri
"""




text="Python"
pattern="th"
x=len(text)
y=len(pattern)
d=256
flag=0

#Find the sum of pattern
sumP=0
for i in range(y):
    sumP=sumP+(ord(pattern[i])*(d**(y-i-1)))
    
#Find sum of text
sumT=0
for i in range(y):
    sumT=sumT+(ord(text[i])*(d**(y-i-1)))
   
if(sumP==sumT):
    print("Pattern is present in the text at",i-y+1)
        
#Rolling Has function
for i in range(y,x):
    sumT=(sumT-(ord(text[i-y]))*(d**(y-1)))*d+ord(text[i])
    if(sumP==sumT):
        print("Pattern is present in the text at",i-y+1)
        flag=1
if flag==0:
    print("Pattern is not present in the text")