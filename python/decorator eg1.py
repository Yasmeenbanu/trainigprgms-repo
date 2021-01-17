# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:05:00 2020

@author: Asifulla K
"""

def print_msg():
    print("hello everyone")
def outer(print1):
    print("outer collected the address")
    def inner():
        print("entering inner")
        ref=print1
        ref()
        print("leaving inner")
    return inner
ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("program completed")