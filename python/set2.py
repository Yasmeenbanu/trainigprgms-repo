# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:11:25 2020

@author: Asifulla K
"""

s1={1,2,3,4,}
s2={3,4,5,6}
s3=s1.union(s2)
print(s3)
s1.intersection_update(s2)
print(s1)
print(s2)
s4={10,20,30,40}
s5={30,40,50,60}
s4.difference_update(s5)
print(s4)
print(s5)
s5.difference_update(s4)
print(s4)
print(s5)
s6={99,88,77,66}
s7={77,66,55,44}
s6.symmetric_difference_update(s7)
print(s6)
print(s7)
