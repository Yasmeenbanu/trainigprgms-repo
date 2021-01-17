# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:59:34 2020

@author: Asifulla K
"""
def func1():
    a=10
    print("from func1 a",a)
    def func2():
        b=20
        print("from func1 a",a)
        print("from func2 b",b)
    func2()
    print("from func1 a",a)
    print("from func2 b",b)
func1()
