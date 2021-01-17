# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:25:27 2020

@author: yasu
"""

class A:
    def __init__(self):
        self.a=10
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b=20
class C(B):
    def __init__(self):
        B.__init__(self)
        self.c=30
c1=C()
print(c1.a)
print(c1.b)
print(c1.c)