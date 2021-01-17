# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:22:07 2020

@author: Asifulla K
"""

str=input("Enter the sting : ")
i=0
Char=0
Digit=0
Symbol=0
while(i<=len(str)-1):
    data=ord(str[i])
    if(data>=65 and data<=90 or data>=97 and data<=122):
        Char=Char+1
    elif(data>=48 and data<=57):
        Digit=Digit+1
    else:
        Symbol=Symbol+1
        
    i=i+1
print("Chars = ",Char)
print("Digits = ",Digit)
print("Symbolss = ",Symbol)