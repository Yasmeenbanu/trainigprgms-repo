# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:58:26 2020

@author: Asifulla K
"""

def mul(num1, num2):
  product = num1 *num2
  if(product > 1000):
    return product
  else:
    return num1 +num2

number1 = 20
number2 = 30

result = (number1*number2)
print("The result is", result)