# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:15:25 2020

@author: Asifulla K
"""

# change the value for a different result
#num = 3

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)