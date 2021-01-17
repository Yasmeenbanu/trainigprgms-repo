# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:14:34 2020

@author: Asifulla K
"""

a=set()
for i in range(5):
    print("enter an element")
    data=int(input())
    a.add(data)
print(a)
a.update([999,888,777])
print(a)
print("enter the element to del")
ele1=int(input())
print(a)
ele2=int(input())
try:
    a.remove(ele2)
    print("ele deleted")
except Exception as e:
    print("ele not present")