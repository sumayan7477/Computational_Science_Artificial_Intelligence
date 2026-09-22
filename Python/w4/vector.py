import numpy as np

# 1D vector
v = np.array([1, 2, 3])
# row vectro
np.array([[1, 2, 3]])
# column vector
np.array([[1], [2], [3]])

# shape of the vector
print(v.shape)
v.reshape(-1, 1)
print(v.shape)

# arrange function
np.arange(1, 10, 2)

# %% Exercise 1
import numpy as np

v1 =np.arange(5, 126, 5)
v2 = np.arange(125, 4, -5)
v3 = np.arange(-100, -50)
v4 = np.linspace(3.1, 43.1, 201)
v5 = np.concatenate([
    np.arange(0,101),
    np.arange(100, -1, -1),
    np.arange(0, 50)
])

v6 = np.concatenate([
    np.arange(0, 64, 2),
    np.arange(60, -5, -2)
])
print(v1 , v2, v3, v4, v5, v6)

# %% exercise 2
import numpy as np
v1 = np.linspace(1, 10, 10)
v2 = np.linspace(0, 10, 11)
v3 = np.linspace(10, 50, 9)
print(v1, v2, v3)

# %% 5.2 Element-wise Operations
# exercise 3
import numpy as np

x2 = np.array([0, 1, 2, 3])
x3 = np.array([1, 2, 3, 4])

print(x2 + 1)
print(x2 * x3)
print(x2 @ x3)
print(x2 ** 2)
print(2 ** x2)
print(12 / x3)
print(x2 / x3)
print(x2 - x3)
print(x2 + x3)
print(2 * x2)
# *  → element-wise multiplication
# @  → dot product / matrix multiplication

# %% exercise 4
import numpy as np

# cos(x)+2x**−3+5x**−2x

x = np.array([1, 3, 5, 7, 9, 3*np.pi])

result = np.cos(x) + 2*x**(-3) + 5*x**(-2*x)

print(result)

# %% exercise 5
import numpy as np

terms = (1/3) ** np.arange(0, 11)
print(terms)

result = np.sum(terms)
print(result)
# using sum
result = sum(terms)
print(result)
# check
formula = (1 - (1/3)**11) / (1 - 1/3)

print(formula)
