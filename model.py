import numpy as np
import math
import params as pms
import plotting as plot
import matplotlib.pyplot as plt
import dc_elements as dc
import ac_elements as ac

def simulate_impedance():

    #generate array of frequencies to use
    start_freq = 100000
    stop_freq = 0.001
    per_decade = 10
    start_b10 = math.log10(start_freq)
    stop_b10 = math.log10(stop_freq)
    no_freqs = (stop_b10 - start_b10) * -1 * per_decade
    freqs = np.logspace(start_b10, stop_b10, num=no_freqs, endpoint=True, base=10)
    
    #calculating phase and magnatude
    phase = np.ones(80)* 30
    magnatude = np.ones(80)

    #calculating Z_real and Z_img
    Z_real = np.ones(80)
    Z_img = np.ones(80)

    plot.bode(freqs, phase, magnatude)
    plot.niquist(Z_real, Z_img)

    return 0

def simulate_lissajous():
    frequency = 100   #Hz
    amplitude = 0.05    #A cm-2
    no_cycles = 5       #cycles to show in plot
    time = np.linspace(0, no_cycles/frequency, 1000)
    current = amplitude*np.sin(time*frequency*2*math.pi) #functions operates in radians

    circuit_1 = ac.resistor(0.1) #instantate cell
    voltage = circuit_1.dc(current) #find voltage

    plot.sino(time, current, voltage)
    plot.lissajous(current, voltage)

def simulate_pol_curve():

    #calculate range of currents to use
    start_current = 0
    stop_current = 2
    current = np.linspace(start_current, stop_current, 100)
    
    #calculate potential 
    voltage_equlib = np.ones(len(current)) * dc.e_equlib()
    eta_membrane = dc.eta_ir(current)
    eta_anode = dc.eta_anode(current)
    eta_cathode = dc.eta_cathode(current)

    #calculate cell voltage
    voltage =   eta_anode + eta_cathode + voltage_equlib + eta_membrane

    plot.dc_plot(current, voltage)
    return 0

#calling functions

#simulate_pol_curve()
simulate_lissajous()
#simulate_impedance()