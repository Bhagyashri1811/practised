# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:27:08 2021

@author: Bhagyashri
"""

import pandas as pd

df = pd.read_excel (r'C:\Users\OWNER\Desktop\SEM 4 BOOKS\Book1.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
print (df)