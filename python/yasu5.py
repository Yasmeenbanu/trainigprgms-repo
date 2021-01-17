# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:21:09 2020

@author: Asifulla K
"""

def operation(data):
    return data+10
L=[]
i=0
while(i<=4):
    print("enter the element")
    num=int(input())
    L.insert(i,num)
    i=i+1
k=list (map (operation,L))
print(k)