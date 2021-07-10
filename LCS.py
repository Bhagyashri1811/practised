# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:14:01 2021

@author: Bhagyashri
"""

def lcs(x,y):
    m=len(x)
    n=len(y)
    L=[0 for i in range(n+1)for j in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i-1]==y[j-i]):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]= max(L[i-1][j],L[i][j-1])
    
    return L[m][n]

x="ABCD"
y="BD"
D= lcs(x, y)