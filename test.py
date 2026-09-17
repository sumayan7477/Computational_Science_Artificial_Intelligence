import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
import pandas

print("Everything is working!")
np.sin(1.2) 
a=1+1
print(a)
x=[1,2,3,4,5]
print(x)
x=np.array([1,2,3,4,5])
print(x)
x2=np.arange(1,101,2)
print(x2)
print(x2.shape)
print(x2.size)
# this is a comment
# %%

print(np.sin(a))
x = np.linspace(-2, 2, 400)
y = x**2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
