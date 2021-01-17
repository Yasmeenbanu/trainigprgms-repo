# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:53:52 2020

@author: Asifulla K
"""

a=[10,20,30,40,50]
a.insert(2,25)
print(a)
a.append(60)
a.append(70)
a.append(80)
#a.append(60,70,80)#error
print(a)
b=[90,100,110]
a.extend(b)
print(a)
a.extend([140,150,160])
print(a)
