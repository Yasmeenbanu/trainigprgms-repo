# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:23:10 2020

@author: Asifulla K
"""

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("Bus", 180, 12)
print(School_bus.seating_capacity())