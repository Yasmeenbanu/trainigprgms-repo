# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:02:04 2020

@author: Asifulla K
"""

class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value

p=Person()
p.setter("Ramu")
msg=p.getter()
print(msg)   
