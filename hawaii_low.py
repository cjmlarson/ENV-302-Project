# MODEL parameters
DAYS = 365 * 500  # run model for this many days
steps_per_day = 24  # run this many simulations per day (i.e. inverse of time step)
location = "Hawaii, 1500m ASL"

# RAINFALL parameters
rainy_days = 73  # average number of rainy days
yearly_rainfall = 3500  # average yearly rainfall in mm

# SOIL MOISTURE parameters
Z = 300  # depth of the soil in mm
n = 0.5  # porosity
s_h = 0.02  # hygroscopic point
s_w = 0.065  # wilting point
s_ast = 0.17  # water stress point
s_fc = 0.3  # field capacity
E_max = 0.8  # max evaporation in/day
T_max = 3.3  # max transpiration in/day
b = 0.2  # soil porosity index
K_s = 1.1  # saturated hydraulic conductivity in/day
s_init = 0.11  # initial soil moisture

# CARBON parameters
ADD = 180/365  # litterfall in gC per day*m^2
k_d = 8.5 * 10 ** (-3)
k_l = 6.5 * 10 ** (-5)
k_h = 2.5 * 10 ** (-6)
r_h = 0.25
r_r = 0.6
C_h_init = 7975  # initial humus carbon gC/m^2
C_b_init = 19  # initial biomass carbon
C_l_init = 1240  # initial litter carbon
