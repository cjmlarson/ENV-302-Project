import numpy as np
from numpy import random as rd

# random seed
rd.seed(69420)

# rainfall metrics from Google
yearly_rainfall = 47  # average yearly rainfall in inches
rainy_days = 102  # average rainy days per year
DAYS_IN_YEAR = 365

# "Poisson" distribution (is actually a binomial approximation)
p_rainy_day = rainy_days / DAYS_IN_YEAR  # probability a day is raining
exp_rain = yearly_rainfall / rainy_days  # expected rainfall on rainy days


# Exponential distribution inverse cdf
def exp(p, mu):
    return -1 * np.log(1 - p) * mu


# list of rainfall metrics
rain_history = []

# Simulate rainy days
for i in range(365):
    rainy = (rd.uniform() < p_rainy_day)
    rainfall = 0

    if rainy:
        rainfall = exp(rd.uniform(), exp_rain)

    print("Day %d: %.2f inches" % (i, rainfall))

    rain_history.append(rainfall)

print("Total rainfall: %.2f inches" % sum(rain_history))
