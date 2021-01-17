# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:36:02 2020

@author: Asifulla K
"""

from PIL import Image
from numpy import*

temp=asarray(Image.open("IMG_20171030_091521_HDR.jpg"))
for j in temp:
    new_temp=asarray([i[0],i[1]]for i in j)# new_temp gets the two first pixel values
    
from PIL import Image 
from numpy import* 
 
temp=asarray(Image.open('test.jpg')) 
x=temp.shape[0] 
y=temp.shape[1]*temp.shape[2] 
 
temp.resize((x,y)) # a 2D array 
print(temp) 
from PIL import Image 
from numpy import* 
 
temp=Image.open('THIS.bmp') 
temp=temp.convert('1')      # Convert to black&white 
A = array(temp)             # Creates an array, white pixels==True and black pixels==False 
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A 
 
for i in range(len(A)): 
    for j in range(len(A[i])): 
        if A[i][j]==True: 
            new_A[i][j]=0 
        else: 
            new_A[i][j]=1