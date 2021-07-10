# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:26:44 2021

@author: Bhagyashri
"""


def mergesort(listA):
    if(len(listA)>1):
        mid = int((len(listA))/2)
        lefthalf= listA[:mid]
        righthalf= listA[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                listA[k]=lefthalf[i]
                i=i+1
            else:
                listA[k]=righthalf[j]
                j=j+1
            k=k+1
        
        while i<len(lefthalf):
            listA[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            listA[k]=righthalf[j]
            j=j+1
            k=k+1

listA=[4,3,1,9,6,5,3]
mergesort(listA)
print(listA)