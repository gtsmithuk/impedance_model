#fundamental constants
F = 96485       #C mol-1
R = 8.314       #J K-1 M-1

#operating constants
T = 25 + 273.15 #K
p_anode = 0.1   #MPa
p_cathode = 0.1 #MPa
j = 1           #A cm-2
RH = 80         #%

#cell constants
cell_area = 1   #cm2
E0 = 0          #Hydrogen on both sides, E0 for both sides 
n = 2           #Electrons
loading =  0.2  #mg cm-2
utilisation = 0.8 # amount of catalyst surface area active

#membrane constants
mem_thickickness = 50 #um
mem_sigma = 0.040 # Ohm cm-2

#catalyst constants, assume symmetrical electrodes
#alpha = 0.5 assumed in physical model
j0 = 0.216 #A cm-2   #A cm-2 for 5wt%, 2.2nm, Pt/C from Gasteiger paper, 
cat_sa = 120    #m2 g-1
electrode_sa = loading/1000 * cat_sa * 10000 * utilisation #cm2

#gas transport layer
gdl_D = 1 #effective mass transport
gdl_thickness = 100e-6 #m
gdl_porosity = 1
gdl_constrictivity = 1
gdl_tortuosity = 1
gdl_D_eff = gdl_D * gdl_porosity * gdl_constrictivity / gdl_tortuosity