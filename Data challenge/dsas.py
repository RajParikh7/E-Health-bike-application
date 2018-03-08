# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 10:50:20 2018

@author: rajpa
"""
count=0
a=["red","orange","Indigo"]
for i in a:
    if "e" in i:
        continue
    print(i)
    count=count+1
print(count)
