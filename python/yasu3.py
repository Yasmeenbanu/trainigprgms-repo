# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:55:58 2020

@author: Asifulla K
"""
def operation(data) :
    return data+10
L=[]
i=0
while(i<=4):
	print("enter an element")
	num=int(input())
	L.insert(i,num)
	i=i+1
i=0
while(i<=4):
    element=L[i]
    newelement=operation(element)
    print(newelement)
    i=i+1
    