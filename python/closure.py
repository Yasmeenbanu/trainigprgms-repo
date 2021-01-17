# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:24:58 2020

@author: Asifulla K
"""

def outer():
    print("entering outer")
    def inner():
        print("entering inner")
        print("processing")
        print("leaving inner")
    return inner
ref=outer()
print("after executing outer")
ref()
print("after executing inner using ref")