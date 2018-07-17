#this document contains equations for calculating the DC overpotential of the reactions

import params as pms
import math
import numpy as np

#calculate equlibrium potential from Nernst Equation
def e_equlib():
    
    voltage = pms.E0 - pms.T * pms.R/ pms.F/ pms.n * math.log(pms.p_anode/pms.p_cathode)
    return voltage

#calculate ir loss from resitance
def eta_ir(current):
    
    voltage = pms.mem_sigma * current
    return voltage

#calculate ir loss from anode overpotential
def eta_anode(current):

    voltage =  [pms.R * pms.T / pms.alpha / pms.F * math.log(pms.i0)] + np.log(current) * pms.R * pms.T / pms.alpha / pms.F
    return voltage

#calculate ir loss from cathode overpotential
def eta_cathode(current):

    voltage =  [pms.R * pms.T / pms.alpha / pms.F * math.log(pms.i0/pms.anode_sa)] + np.log(current/pms.anode_sa) * pms.R * pms.T / pms.alpha / pms.F
    return voltage