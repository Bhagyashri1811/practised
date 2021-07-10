# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 23:04:21 2021

@author: Bhagyashri
"""
from collections import Counter 
import random

n= int(input("Enter the nos of data you want : "))
x=[]
total_x =0
  
for i in range(1,n+1):
    a=random.randint(1, 7)
    x.append(a)
    
elements_count = {}
# iterating over the elements for frequency
for element in x:
   # checking whether it is in the dict or not
   if element in elements_count:
      # incerementing the count by 1
      elements_count[element] += 1
   else:
      # setting the count to 1
      elements_count[element] = 1
# printing the elements frequencies

""" MEAN """
print("*"*25)
print("----Frequency Table----")
print("*"*25)
print("Data    | Frequency")
for key, value in elements_count.items():
   print(f" {key}    |  {value}")
    
for i in range(len(x)):   # Find the total of X nad y
    total_x = total_x + x[i]
    
mean_x = (total_x/len(x))  # Find the mean of x
print("The mean of the Given data is ",round(mean_x,3))


"""  Median """

A= sorted(x)
length=len(x)

if length%2==0:
    median1 = A[length//2] 
    median2 = A[length//2 - 1] 
    median = (median1 + median2)/2
    print("The median of the Data is:", round(median,2))
else:
    median = A[length//2] 
    print("The median of the Data is:", round(median,2))


""" MODE """

data = Counter(A) 
get_mode = dict(data) 
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
if len(mode) == length: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode of the given data is/are : " + ', '.join(map(str, mode)) 
      
print(get_mode) 
