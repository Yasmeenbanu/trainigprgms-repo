# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:25:50 2020

@author: Asifulla K
"""

result_str=""
for row in range(0,7):
    for column in range(0,7):
        if(((column==1 or column==5) and row!=0) or ((row==0 or row==3) and (column>1 and column<5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)