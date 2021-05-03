# MODEL parameters
DAYS = 365 * 20  # run model for this many days
steps_per_day = 24  # run this many simulations per day (i.e. inverse of time step)

# RAINFALL parameters
rainy_days = 83.95  # average number of rainy days
yearly_rainfall = 923.45  # average yearly rainfall in mm

# SOIL MOISTURE parameters
Z = 0.8 * 1000  # depth of the soil in mm
n = 0.4  # porosity
s_h = 0.02  # hygroscopic point
s_w = 0.065  # wilting point
s_ast = 0.17  # water stress point
s_fc = 0.3  # field capacity
E_max = 0.9  # max evaporation in/day
T_max = 3.6  # max transpiration in/day
b = 0.2  # soil porosity index
K_s = 1.1  # saturated hydraulic conductivity in/day
s_init = 0.11  # initial soil moisture

# CARBON parameters
ADD = 1.5  # litterfall in gC per day*m^2
k_d = 8.5 * 10 ** (-3)
k_l = 6.5 * 10 ** (-5)
k_h = 2.5 * 10 ** (-6)
r_h = 0.25
r_r = 0.6
C_h_init = 8500  # initial humus carbon gC/m^3
C_b_init = 80  # initial biomass carbon
C_l_init = 1200  # initial litter carbon
