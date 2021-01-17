# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:03:15 2020

@author: Asifulla K
"""
l=set()
#l=set([1,2,3,4,5,6])
for i in range(6):
    print("enter the book")
    #print(l)
    data=int(input())
    l.add(data)
print(l)
l.update([7,8,9])
print(l)
print("enter the book1 to delete")
book=int(input())
print(l)

try:
    l.remove(book)
    print("book deleted")
except Exception as e:
    print("book not present")
