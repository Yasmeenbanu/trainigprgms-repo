# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:23:47 2020

@author: Asifulla K
"""
class Getprint:
    def __init__(self):
        self.str=""
    def getString(self):
        self.str=input("Enter the String : ")
    def printString(self):
        print("String is ",self.str.upper())
g=Getprint()
g.getString()
g.printString()
