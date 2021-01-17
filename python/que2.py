# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:20:45 2020

@author: Asifulla K
"""

num=int(input("Enter the number: "))
temp=num
reverse=0
while(num>0):
    remainder = num % 10
    reverse=reverse*10+remainder
    num=num//10
rev=reverse
if(rev==temp):
    print("The Original and Reverse number is same ")
else:
    print("The Original and Reverse number is not same ")