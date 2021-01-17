# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:22:21 2020

@author: Asifulla K
"""
#Write a function that prints out the odd numbers 1 through 99. Bonus: Use list comprehension.
# list of numbers 
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,6263,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99] 
  
only_odd = [num for num in list1 if num % 2 == 1] 
  
print(only_odd) 
print()
#Write a function that takes in a dictionary and outputs the most frequent value in the dictionary.
input_dict = {'A': 1963, 'B': 1963,
    'C': 1964, 'D': 1964, 'E': 1964,
    'F': 1965, 'G': 1965, 'H': 1966,
    'I': 1967, 'J': 1967, 'K': 1968,
    'L': 1969 ,'M': 1969,
    'N': 1970}


trk={}

for key,value in input_dict.items():
    if value not in trk:
        trk[value]=0
    else:
        trk[value]+=1

print(max(trk,key=trk.get))
print()
#Write a function to reverse a string. The string can be of any length and might be empty. Bonus: Implement recursively.
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))
print()
#Write a function that takes in two sorted lists and merges them (don’t use any Python built in functions or methods, such as the list.sort method). So the input ([1, 5, 8], [4, 7, 10, 12]) should yield the output [1, 4, 5, 7, 8, 10, 12]. The lists may not be of the same length, and one or both may be empty.
a = [1, 5, 8]
b = [4, 7, 10, 12]
c=a+b
c.sort()
print(a)
print(b)
print(c)