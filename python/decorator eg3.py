# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:13:54 2020

@author: Asifulla K
"""

def outer(print1):
    def inner():
        ref1=print1
        msg1=ref1()
        newstr1=msg1.upper()
        print(newstr1)
    return inner
@outer
def print_morning():
    msg="good morning"
    return msg
@outer
def print_noon():
    msg="good noon"
    return msg
@outer
def print_eve():
    msg="evening"
    return msg
@outer
def print_night():
    msg="good night"
    return msg
print_morning()
print_noon()
print_eve()
print_night()