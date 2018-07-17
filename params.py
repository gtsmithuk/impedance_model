#operating constants
T = 80 + 273.15 #K
R = 8.314       #J K-1 M-1
p_anode = 0.1   #MPa
p_cathode = 100 #MPa
current = 1     #A cm-2
RH = 80         #%

#cell constants
cell_area = 1   #cm2
E0 = 0          #Hydrogen on both sides, E0 for both sides 
n = 2           #Electrons
loading =  0.2  #mg cm-2
utilisation = 0.8 # amount of catalyst surface area active

#material constants
mem_thickickness = 50 #cm

alpha = 0.5     #for 5wt%, 2.2nm, Pt/C from Gasteiger paper
i0 = 0.216      #A cm-2 for 5wt%, 2.2nm, Pt/C from Gasteiger paper
cat_sa = 120    #m2 g-1

#fundamental constants
F = 96485       #C mol-1

#derived constants
#anode catalyst layer
anode_sa =  loading/1000 * cat_sa * 10000 * utilisation #cm2

#cathode catalyst layer
cathode_sa = loading/1000 * cat_sa * 10000 * utilisation #cm2

#membrane
mem_sigma = 0.040 # Ohm cm-2