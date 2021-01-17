# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:01:28 2020

@author: Asifulla K
"""

value = input("Enter value: ")
total=0
for i in range(1,5):
    n1=value*i
    total=total+int(n1)
print(total)