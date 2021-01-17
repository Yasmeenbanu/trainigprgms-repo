# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:07:06 2020

@author: Asifulla K
"""

a={10,20,70,10,50,80,90,70}
print(type(a))
print(a)
#print(a[4])#typeerror;ndexing not allowed
#a[2:4]a[ :8]#slicing not allowed
for data in a:
    print(data)
for index , data in enumerate(a):
    print(index,"",data)

