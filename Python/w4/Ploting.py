# Plotting in Python

import numpy as np
import matplotlib.pyplot as plt

# plt.plot(x, y)
# plt.plot(x, y, '*')    # star markers
# plt.plot(x, y, 'o')    # circles
# plt.plot(x, y, 'r')    # red line
# plt.plot(x, y, '--')   # dashed line
# plt.plot(x, y, 'ro')   # red circles

# exercise 1
# a
x = np.array([0, 1, 2])
y = np.array([5, 4, 3])

plt.plot(x, y, 'ro')
plt.plot(x, y, 'r')
plt.show()
# b
x = np.array([-2, 5])
y = np.array([3, 6])

plt.plot(x, y, 'b')
plt.show()

# c
x = np.arange(-5, 5.01, 0.01)
y = np.sin(x)

plt.plot(x, y)
# plt.show()

# d
x1 = np.arange(-5, 5.01, 0.01)
y1 = x**2
plt.figure()
plt.plot(x1, y1)
plt.show()

# %% Multiple plots in ONE figure
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2])
y = np.array([5, 4, 3])

plt.plot(x, y, 'ro')
plt.plot(x, y, 'b')
plt.plot([1, 5], [5, 5], 'b')

plt.show()

# %%
# New figure = separate graph  plt.figure()
# Select an existing figure  plt.figure(2)/ plt.figure('my figure')

# exercise 2
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5.01, 0.01)
y = x**2

plt.plot(x, y)

# x-axis
plt.plot([-5, 5], [0, 0], 'k')

# y-axis
plt.plot([0, 0], [0, 25], 'k')

plt.show()

# exercise 3
x = np.arange(-5, 5.01, 0.01)

plt.plot(
    x, x**2,
    [-5, 5], [0, 0],
    [0, 0], [0, 25]
)

plt.show()

#  exercise 4 pnly one vectro
y = np.array([5, 2, 8, 4])
plt.plot(y)
plt.show()

# %% parametric plot
import numpy as np
import matplotlib.pyplot as plt

# x=cos(t),y=sin(t)

t = np.arange(0, 2*np.pi, 0.01)

x = np.cos(t)
y = np.sin(t)

plt.plot(x, y)
plt.axis('equal')


# exercise 5
t = np.arange(0, 8*np.pi, 0.01)

x = t**5 * np.cos(t)
y = t**5 * np.sin(t)

plt.plot(x, y)
plt.axis('equal')
plt.show()

# exercise 6

# a
# '-'     # solid line
# '--'    # dashed
# ':'     # dotted
# '-.'    # dash-dot

# 'o'     # circle
# '*'     # star
# '.'     # point
# 's'     # square
# '^'     # triangle

# 'r' → red
# 'g' → green
# 'b' → blue
# 'k' → black
# 'y' → yellow
# 'm' → magenta
# 'c' → cyan
plt.plot(x, y, 'r--') #red + dashed line
plt.plot(x, y, 'bo') #blue + circles

# b
plt.plot(x, y)
plt.plot(x, y+1)
plt.plot(x, y+2)
plt.show()
