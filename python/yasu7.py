# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:21:09 2020

@author: Asifulla K
"""

def outerfunction():
    print("inside outer function")
    def innerfunction():
        print("inside inner function")
    innerfunction()
outerfunction()
innerfunction()


