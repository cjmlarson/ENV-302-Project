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


# run simulation
rainfall = sim_rain()

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
