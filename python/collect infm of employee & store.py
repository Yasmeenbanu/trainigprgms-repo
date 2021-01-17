# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:45:53 2020

@author: Asifulla K
"""

print("enter the filename")
fname=input()
fptr=open(fname,"w")
for i in range(5):
    print("enter the name")
    name=input()
    print("enter the id")
    id=input()
    print("ener the place")
    place=input()
    print("enter the phnum")
    phnum=input()
    data=name+""+id+""+place+""+phnum
    fptr.write(data +"\n")
    fptr.close()
    print("emp rec written to file")