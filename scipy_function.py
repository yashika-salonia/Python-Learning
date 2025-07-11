#find mean, median standard deviation
#use numpy as np then
# np.mean, np.median, np.var, np.std

# lambda command
# use scipy.optimize .maximize to find the minimum value of fx=x^2 + 5*sin(x)

from scipy.optimize import minimize
import numpy as np
import math

a=minimize(lambda x: (x**2) + (5*math.sin(x)) ,x0=0)
print(a)

