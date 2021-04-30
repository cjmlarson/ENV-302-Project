import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

# random seed
rd.seed(69420)

# number of days to simulate
N = 365

# rainfall metrics from Google
yearly_rainfall = 47  # average yearly rainfall in inches
rainy_days = 102  # average rainy days per year
DAYS_IN_YEAR = 365

# "Poisson" distribution (is actually a binomial approximation)
p_rainy_day = rainy_days / DAYS_IN_YEAR  # probability a day is raining
exp_rain = yearly_rainfall / rainy_days  # expected rainfall on rainy days


# Exponential distribution inverse cdf
def inv_exp(p, mu):
    return -1 * np.log(1 - p) * mu


# function to get list of rainfall amounts
def sim_rain():
    # list of rainfall metrics
    rain_history = []

    # Simulate rainy days
    for i in range(N):
        rainy = (rd.uniform() < p_rainy_day)
        rain = 0

        if rainy:
            rain = inv_exp(rd.uniform(), exp_rain)

        rain_history.append(rain)

    return rain_history


# plot daily and cumulative rainfall
def rain_plots(rainfall):
    # plot daily rainfall
    plt.plot(range(N), rainfall)
    plt.title("Daily Rainfall in Princeton, NJ")
    plt.xlabel("Day of year")
    plt.ylabel("Inches of rain")
    plt.show()
    plt.close()

    # plot cumulative rainfall
    plt.plot(range(N), [sum(rainfall[:i]) for i in range(N)])
    plt.title("Cumulative Rainfall in Princeton, NJ")
    plt.xlabel("Day of year")
    plt.ylabel("Inches of rain")
    plt.show()
    plt.close()


# %%

# soil moisture box model setup
# parameters (all quantities normalized per unit area)
Z = 12  # depth of the soil in inches
n = 0.5  # porosity
s_h = 0.1  # hygroscopic point
s_w = 0.2  # wilting point
s_ast = 0.3  # water stress point
s_fc = 0.5  # field capacity
E_max = 0.04  # max evaporation in/day
T_max = 0.16  # max transpiration in/day
b = 0.2  # soil porosity index
K_s = 1  # saturated hydraulic conductivity in/day

# modeled quantity
s = 0  # relative soil moisture

# infiltration (h is storm rainfall)
I = lambda s, h: min(h, n * Z * (1 - s))


# evaporation
def E(s):
    if s < s_h:
        return 0
    elif s < s_w:
        return E_max * (s - s_h) / (s_w - s_h)
    else:
        return E_max


# transpiration
def T(s):
    if s < s_w:
        return 0
    elif s < s_ast:
        return T_max * (s - s_w) / (s_ast - s_w)
    else:
        return T_max


# leakage
def L(s):
    beta = 2 * b + 4

    if s < s_fc:
        return 0
    else:
        return K_s * (np.exp(beta * (s - s_fc)) - 1) / (np.exp(beta * (1 - s_fc)) - 1)


# %%

plt.plot([i / 100 for i in range(100)], [L(i / 100) + E(i / 100) + T(i / 100) for i in range(100)])
plt.show()