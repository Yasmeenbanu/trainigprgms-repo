# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:09:15 2020

@author: Asifulla K
"""

def outer(print1):
    print("outer collected the address")
    def inner():
        print("entering inner")
        ref1=print1
        msg1=ref1()
        newstr1=msg1.upper()
        print(newstr1)
    return inner
@outer
def print_msg():
    msg="hello everyone"
    return msg
print_msg()
print("program completed")