import matplotlib.pyplot as plt
import params as pms

#plot bode
def bode(freqs, phase, magnatude):
    
    fig, ax1 = plt.subplots()
    color = 'blue'
    ax1.set_xlabel('frequency \ Hz')
    ax1.set_ylabel('phase \ $\degree$', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim([0,90])
    ax1.semilogx(freqs, phase, color=color)
    
    ax2 = ax1.twinx()
    color = 'green'
    ax2.set_ylabel('magnatude \ m$\Omega$ cm$^{2}$', color = color)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.semilogx(freqs, magnatude, color=color)

    plt.show()
    plt.close()
    return 0

#plot niquist
def niquist(Z_Real, Z_Img):

    plt.plot(Z_Real, Z_Img)
    plt.xlabel(' Z$_{real}$ \ m$\Omega$ cm$^{2}$')
    plt.ylabel(' Z$_{img}$ \ m$\Omega$ cm$^{2}$') 
    plt.axis('equal')
    plt.legend()
    plt.show()
    plt.close()
    return 0

#plot dc
def dc_plot(current, voltage):

    plt.plot(current/pms.cell_area, voltage*1000)
    plt.xlabel(' Current \ A cm$^{2}$')
    plt.ylabel(' Voltage \ mV') 
#    plt.ylim([0,250])
#    plt.xlim([0,2])
    plt.legend()
    plt.show()
    plt.close()
    return 0
