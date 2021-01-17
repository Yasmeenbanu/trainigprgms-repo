# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:43:29 2020

@author: Asifulla K
"""
class GreaterException(Exception):
    def __init__(self,message):
        self.msg=message
    def __str__(self):
        return self.msg
L=[]
i=0
sum=0
while(i<=10):
    print("enter an element")
    data=int(input())
    L.insert(i,data)
    sum=sum+data
    i=i+1
print("sum is", sum)
try:
    if(sum>50):
        e=GreaterException("error, value>50")
        raise e
    else:
        print("the value is less than or equal to 50")
except Exception as e:
    print(e)    