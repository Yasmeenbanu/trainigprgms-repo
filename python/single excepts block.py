# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:37:05 2020

@author: Asifulla K
"""

try:
    print("enter an elemet")
    a=int(input())
    print("enter an element")
    b=int(input())
    res=a/b
    print(res)
except (ZeroDivisionError,ValueError) as e:
    print('i/p not proper" or Division Error)
    print("program leaving manually")