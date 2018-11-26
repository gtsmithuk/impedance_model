import matplotlib.pyplot as plt
import params as pms
import numpy as np

#plot bode
def bode(freqs, phase, magnatude):
    
    fig, ax1 = plt.subplots()
    color = 'blue'
    ax1.set_xlabel('frequency / Hz')
    ax1.set_ylabel('phase / $\degree$', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim([0,90])
    ax1.semilogx(freqs, phase, color=color)
    
    ax2 = ax1.twinx()
    color = 'green'
    ax2.set_ylabel('magnatude / m$\Omega$ cm$^{2}$', color = color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.semilogx(freqs, magnatude, color=color)

    plt.show()
    plt.close()
    return 0

#plot niquist
def niquist(Z_Real, Z_Img):

    plt.plot(Z_Real, Z_Img)
    plt.xlabel(' Z$_{real}$ / m$\Omega$ cm$^{2}$')
    plt.ylabel(' Z$_{img}$ / m$\Omega$ cm$^{2}$') 
    plt.axis('equal')
    plt.legend()
    plt.show()
    plt.close()
    return 0

#plot dc
def dc_plot(current, voltage):

    plt.plot(current/pms.cell_area, voltage*1000, 'o')
    plt.xlabel(' Current / A cm$^{2}$')
    plt.ylabel(' Voltage / mV')
    #plt.ylim(0,200)
    plt.legend()
    plt.show()
    plt.close()
    return 0

#tafel
def tafel(current, voltage):

    plt.plot(np.log(current),voltage*1000, 'o')
    plt.xlabel('log(i)')
    plt.ylabel('Voltage / mV')
    plt.legend()
    plt.show()
    plt.close()
    return 0

#time
def sino(time, current, voltage):

    fig, ax1 = plt.subplots()
    color = 'red'
    ax1.set_xlabel('Time / s')
    ax1.set_ylabel('Current / A cm$^{2}$', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.plot(time, current/pms.cell_area, color=color, label='Current')
    
    ax2 = ax1.twinx()
    color = 'blue'
    ax2.set_ylabel('Potential / mV', color = color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.plot(time, voltage*1000, color=color, label = 'Voltage')
    plt.show()
    plt.close()
    return 0

# lissajous plot
#def lissajous():

#    current = {}
#    voltage = {}
#    frequency = {}
    
<<<<<<< HEAD
    plt.plot(current, voltage, '-', label=frequency)
=======
#    for i in :
#        plt.plot(current, voltage, '-', label=frequency)
>>>>>>> f05584b99c2a1acc1052118b2d339d4f666f3649

    plt.xlabel('Current / A cm$^{2}$')
    plt.ylabel('Potential / mV')
    plt.legend()
    plt.show()
    plt.close()
    return 0