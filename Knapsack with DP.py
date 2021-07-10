# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:09:33 2021

@author: Bhagyashri
"""

def knapsack(val,wt,W,n):
    if n==0 or W==0:
        return 0
    if(wt[n-1]>W):
        return knapsack(val, wt, W, n-1)
    else:
        return max(knapsack(val, wt, W, n-1),knapsack(val, wt, W-wt[n-1], n-1)+val[n-1])
    
    
val=[15,12,9,16,17]
wt=[2,5,3,4,6]
n=len(val)
W=12
print(knapsack(val, wt, W, n))