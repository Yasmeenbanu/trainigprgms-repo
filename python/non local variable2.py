# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:04:06 2020

@author: Asifulla K
"""

def func1():
    a=10
    print("before",a)
    def func2():
        a=999
        b=20
        print("func2 a",a)
        print("func2 b",b)
    func2()
    print("after",a)
func1()