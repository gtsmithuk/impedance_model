#this document contains equations for calculating the impedance of specific elements

import params as pms
import math
import numpy as np

#resistor
class resistor:
    def __init__(self, resistance):
        self.resistance = resistance
    
    def dc(self, current):
        voltage = current * self.resistance
        return voltage

#capacitor
class capacitor:
    def __init__(self, capacitance):
        self.capacitance = capacitance
    
    def dc(self, current):
        voltage = current * self.capacitance
        return voltage

#inductor
class inductor:
    def __init__(self, inductance):
        self.inductance = inductance
    
    def dc(self, current):
        voltage = current * self.inductance
        return voltage