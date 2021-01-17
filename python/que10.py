# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:42:54 2020

@author: Asifulla K
"""
string=input("Enter the string : ")
Ucount=0
Lcount=0
count=0
i=0
while(i<=len(string)-1):
    data=ord(string[i])
    if(data>=65 and data<=90):
        Ucount=Ucount+1
    else:
        Lcount=Lcount+1
    count=count+1
    i=i+1
print("Number of uppercase leters are : ",Ucount)
print("Number of lowercase leters are : ",Lcount)
print("Total letters:",count)
