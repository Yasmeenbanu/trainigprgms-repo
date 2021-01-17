# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:05:05 2020

@author: Asifulla K
"""

class animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
         print("animal is sleeping")
    def breathe(self):
        print("animal is breathing")
class tiger(animal):
    def eat(self):
        print("tiger is eating")
    def sleep(self):
         print("tiger is sleeping")
    def breathe(self):
        print("tiger is breathing")
class deer(animal):
    def eat(self):
        print("deer is eating")
    def sleep(self):
         print("deer is sleeping")
    def breathe(self):
        print("deer is breathing")
class monkey(animal):
    def eat(self):
        print("monkey is eating")
    def sleep(self):
         print("monkey is sleeping")
    def breathe(self):
        print("monkey is breathing")
t=tiger()
d=deer()
m=monkey()
def allowanimals(ref):
    ref.eat()
    ref.sleep()
    ref.breathe()
allowanimals(t)
print()
allowanimals(d)
print()
allowanimals(m)