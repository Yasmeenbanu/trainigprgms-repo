# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:07:36 2020

@author: Asifulla K
"""

s1={1,2,3,4,}
s2={3,4,5,6}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)
s6=s2.difference(s1)
print(s6)
s7=s1.symmetric_difference(s2)
print(s7)

