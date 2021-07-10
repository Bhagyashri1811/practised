# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:53:16 2021

@author: Bhagyashri
"""

# Recursive Binary Search 
def binary_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return mid
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high)


data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37
print("Th elemnet found at",binary_search_recursive(data, target, 0, len(data)-1))