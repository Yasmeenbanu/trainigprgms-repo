# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:23:37 2020

@author: Asifulla K
"""
class A:
    def dispA(self):
        print("inside dispA")
class B(A):
    def dispB(self):
        print("inside dispB")
c1=A()
c1.dispA()
c1.dispA()

