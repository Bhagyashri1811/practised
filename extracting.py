# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:39:54 2021

@author: prera
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#opening and reading excel file
df = pd.read_csv (r'D:\additional_measures_cleaned.csv')


df1 = pd.DataFrame(df)
print(df1)

#extracting particular column
df2 = df1['Physical Inactivity']
df3 = pd.DataFrame(df2)
arr = np.sort(np.array(df3))

df4 =  df3['Physical Inactivity'].unique()
df5 = (np.array(df4))
#print("value",df5)

df6 = df3['Physical Inactivity'].value_counts()
df7 = (np.array(df6))
#print("np",df7)




plt.xlabel("marks")
plt.ylabel("frequency")

print("scattering")
plt.scatter(df5,df7)
plt.show()

print("bar graph")
plt.bar(df5,df7,width=0.4,color="green")
plt.show()

print("histogram")
bins = [0,5,10,15,20]
plt.hist(df7,bins,histtype='bar',rwidth=0.8,color="red")
plt.show()

print("pie chart")
plt.pie(df7,labels=df5,autopct='%1.1f%%',startangle=90)
plt.show()

print("box plot")
plt.boxplot(arr)
plt.show()

print("quartiles")
q1 = np.percentile(arr,25)
print("25",q1)
q2 = np.percentile(arr,75)
print("75",q2)
q3 = np.percentile(arr,50)
print("50",q3)

print("cummulative graph")
values, base = np.histogram(df7, bins)
cumulative = np.cumsum(values)
plt.plot(base[:-1],cumulative, 'ro-')
plt.show()

print("line bar graph")
values, base = np.histogram(df5,bins)
plt.plot(base[:-1],values, 'bo-')
plt.show()

