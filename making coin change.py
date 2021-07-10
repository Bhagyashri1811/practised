# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:05:21 2021

@author: Bhagyashri
"""

def makingcoinchange(coin,amt):
    table=[0 for i in range(amt+1)]
    table[0]=1
    for i in range(len(coin)):
        for j in range(coin[i],amt+1):
            table[j]+=table[j-coin[i]]
    return table[amt]

coin=[2,3,5,10]
amt=15
print("The comination are: ", makingcoinchange(coin, amt))    