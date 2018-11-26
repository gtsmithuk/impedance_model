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
    j = current/pms.electrode_sa #specific current density
    b =  2 * pms.R * pms.T / pms.n / pms.F
    voltage = np.arcsinh(j/2/pms.j0) * b
    return voltage

#calculate ir loss from cathode overpotential
def eta_cathode(current):
    j = current/pms.electrode_sa #specific current density
    b =  2 * pms.R * pms.T / pms.n / pms.F
    voltage = np.arcsinh(j/2/pms.j0) * b
    return voltage

#calculate polarisation loss
def eta_conc_anode(current):
    i_lim = pms.n * pms.F * pms.gdl_D_eff * pms.p_anode / pms.gdl_thickness
    voltage = -pms.R * pms.T / pms.n / pms.F * np.log(1- current / i_lim)
    return voltage

#calculate crossover loss diffusion and permeability
def eta_crossover(current):
    diffusion = 1
    permeability = 1 
    voltage = diffusion + permeability
    return voltage