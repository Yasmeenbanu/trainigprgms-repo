# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:25:27 2020

@author: yasu
"""

class parent:
    def __init__(self):
        self.a=10
class child(parent):
    def __init__(self):
        parent.__init__(self)
        self.b=20
c=child()
print(c.a)
print(c.b)