# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:41:16 2020

@author: Asifulla K
"""
def reverse_list1(list1):
    reversed_list1=[]
    for i in reversed(list1):
        reversed_list1.append(i)
    print("list1:", list1)
    print("reverse list1:", reversed_list1)
list1 = [10, 20, 30, 40, 50]
reverse_list1(list1)