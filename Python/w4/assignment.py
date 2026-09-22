# task 1
import numpy as np
import matplotlib.pyplot as plt

# 1b  ***********************************
v = np.array([1, 2, 3])
print(v)

# 1c
v1 = np.arange(1, 11)
v2 = np.arange(10, 2) # []
v3 = np.arange(1, 11, 2)
v4 = np.arange(-23, 1, 3)
v5 = np.arange(1000, 949, -10)
v6 = np.concatenate((np.arange(1, 6),
                     np.arange(5, -1, -1)))

# i  **************************************
x1 = np.arange(5, 126, 5)
# ii
x2 = np.arange(125, 0, -5)
# iii
x3 = np.arange(-100, -50)
# iv
x4 = np.arange(3.1, 43.2, 0.2)
# v
x5 = np.concatenate((
    np.arange(0, 101),
    np.arange(100, -1, -1),
    np.arange(0, 50)
))
# vi
x6 = np.concatenate((
    np.arange(0, 63, 2),
    np.arange(60, -6, -2)
))

# 1d **********************************
f1 = np.array([
    np.sum(x1),
    np.sum(x2),
    np.sum(x3),
    np.sum(x4),
    np.sum(x5),
    np.sum(x6)
])

print(f1)

f2 = np.mean(f1)

print(f2)

# %%%%%%%%%%%%%%%%%%% Task 2 %%%%%%%%%%%%%%%%%%%%%%
import numpy as np

# 2b ************
x1 = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

print(x1)
print(np.sin(x1))

# The tiny numbers such as: 1.22464680e-16 are basically 0. They appear because computers use floating-point numerical calculations.

# 2c ************
x = np.array([
    np.pi,
    2*np.pi,
    3*np.pi,
    4*np.pi,
    5*np.pi
])

print(np.sin(x))
# These are numerical errors extremely close to zero.


# 2d ************
prod = x1*x1
print(prod)
# This is element-by-element multiplication 

# 2e ************
x2 = np.array([0, 1, 2, 3])
x3 = np.array([1, 2, 3, 4])

print(x2+1)
print(x2*x3)
print(x2**2)
print(x2/x3)
print(x2-x3)

# 2f ************
x = np.linspace(-5, 5, 10)

y = np.sin(x) / x

print(x)
print(y)

# %% Matplotlib TASK 3 %%%%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([-3, -1, 0, 1, 3])
y1 = np.array([7, 3, 7, 3, 7])


# 3a  **************
x = np.array([0, 1, 2])
y = np.array([5, 4, 3])

# plt.plot(x, y, 'ro')
# plt.show()
# to connect with lines 
plt.plot(x, y, 'r-o')
plt.show()



# 3b  **************
x2 = np.linspace(-5, 5, 1000)
y2 = np.sin(x2)

plt.figure()
plt.plot(x2, y2)
plt.show()

# np.arange(-5, 5.5, 0.5)  have about 21 points.  np.linspace(-5, 5, 1000) have 1000 point
# Matplotlib connects the points with straight line segments. More points → shorter segments → curve looks smooth.
 

# %% Task 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
import numpy as np

u = np.array([1, 2, 3])
v = np.array([-2, -3, 1])

# 4a *************
sum_uv = u + v
print(sum_uv)

diff_uv = u - v
print(diff_uv)

linear = 2*u - 3*v
print(linear)

# 4b ***********
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print(norm_u)
print(norm_v)


# 4c ************
unit_u = u / np.linalg.norm(u)
unit_v = v / np.linalg.norm(v)

print(unit_u)
print(unit_v)

# 4d ***************
dot_product = np.dot(u, v)

print(dot_product)

angle = np.degrees(
    np.arccos(
        np.dot(u, v) /
        (np.linalg.norm(u) * np.linalg.norm(v))
    )
)

print(angle)

# 4e ************

uxv = np.cross(u, v)
vxu = np.cross(v, u)

print(uxv)
print(vxu)

# %%
