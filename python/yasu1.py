# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:55:58 2020

@author: Asifulla K
"""
def even(num):
    if(num%2==0):
        return True
    else:
        return False
L=[]
i=0
while(i<=4):
	print("enter an element")
	num=int(input())
	L.insert(i,num)
i=0
while(i<=4):
    data=L[i]
    status=even(data)
    if(status==true):
        print(L[i])
    i=i+1
    