import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.optimize as optimize
import time
import math


#%% define a function with lambda function ----------

f = lambda x: 1 / (x + 0.5) ** 2 + x

# add domain

x = np.linspace(0 , 4, 100)
y = f(x)

#plotting

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Exercise 1")
plt.grid(True)
plt.legend()
plt.show()

# %% Population problem
import numpy as np
n0 = 1.0
half_life = 70.0

lam = np.log(2) / half_life

N = lambda t: n0*np.exp(-lam*t)

amount_100 = N(100)
print(f"Decay constant (lambda): {lam}")
print(f"Amount after 100 time units: {amount_100}")


# %% problem 3 loop vs vectorization
import time
import numpy as np

f = lambda x: np.cos(x) + np.log(x)


t0 = time.time()
x_array = np.arange(0.1, 100, 0.01)

# using numpy
res_vec = f(x_array)
t1 = time.time()
time_vec = time.time() - t0

# using loop
res_loop = []
for val in x_array:
    res_loop.append(f(val))
time_loop = time.time() - t0

print(f"Vectorized time: {time_vec:.6f} seconds")
print(f"For-loop time:   {time_loop:.6f} seconds")


# %% problem 4 integration
import numpy as np


