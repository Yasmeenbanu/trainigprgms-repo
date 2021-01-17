# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:16:59 2020

@author: Asifulla K
"""

class cargoplane:
    def takeoff(self):
        print("plane tookoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carrycargo(self):
        print("carring cargo")
class passengerplane:
    def takeoff(self):
        print("plane tookoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carrypassenger(self):
        print("carring passenger")
class fighterplane:
    def takeoff(self):
        print("plane tookoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
    def carryfighter(self):
        print("carring weapons")
c=cargoplane()
p=passengerplane()
f=fighterplane()
c.takeoff()
c.fly()
c.land()
c.carrycargo()
print()
p.takeoff()
p.fly()
p.land()
p.carrypassenger
print()
f.takeoff()
f.fly()
f.land()       
f.carryfighter()