# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:39:41 2021

@author: Bhagyashri
"""

def partition(arr,low,high):
    pivot=arr[high]
    pindex=low
    for j in range(low,high):
        if(arr[j]<pivot):
            arr[j],arr[pindex]=arr[j],arr[pindex]
            pindex=pindex+1
    arr[pindex],arr[high]=arr[high],arr[pindex]
    return pindex

def quicksort(arr,low,high):
    pindex=partition(arr, low, high)
    quicksort(arr, low, pindex-1)
    quicksort(arr, pindex+1, high)



arr=[9,5,38,22,4,6,223,59,2239,0]
n=len(arr)
quicksort(arr,0,n-1)
print(arr)