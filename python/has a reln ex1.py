# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:33:59 2020

@author: Asifulla K
"""

class radio:
    def turnon(self,x):
        if(x==1):
            print("radio is on")
        else:
            print("radio is off")
class car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=radio()
c=car(60,100)
print(c.min)
print(c.max)
c.r.turnon(1)