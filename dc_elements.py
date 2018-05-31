#this document contains equations for calculating the DC overpotential of the reactions

import params as pms
import math

#calculate equlibrium potential from Nernst Equation
def e_equlib():
    
    voltage = pms.E0 - pms.T * pms.R/ pms.F/ pms.n * math.log(pms.p_anode/pms.p_cathode)
    return voltage

#calculate ir loss from current and resitance
def eta_ir(current):
    
    voltage = pms.mem_sigma * current
    return voltage

#calculate ir loss from current and resitance
def eta_anode(current):
    
    voltage = 
    return voltage

#calculate ir loss from current and resitance
def eta_cathode(current):
    
    voltage = 
    return voltage