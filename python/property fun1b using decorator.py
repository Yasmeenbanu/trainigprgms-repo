# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:21:52 2020

@author: Asifulla K
"""
class Person:
    def __init__(self):
        self.__name=""
    @property
    def empName(self):
        return self.__name
    @empName.setter
    def empName(self,value):
        self.__name=value

p2=Person()
p2.empName="Rohan"
msg=p2.empName
print(msg)

