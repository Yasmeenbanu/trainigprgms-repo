# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:24:39 2020

@author: Asifulla K
"""

class Example:
    def __init__(self):
       self.string=""
        
    def getInput(self):
        self.string=input("Enter the input string : ")
    def display(self):
        print("the String is : ",self.string)
        
c=Example()
c.getInput()
c.display()