import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# ==========================================
# Task 1: Updating Sequences with For Loops
# ==========================================

# a
a= 1
for i in range(1,21):
    a= 2*a
print(f"1(a) a_20 = {a}")

# b
a= 1
for n in range(1,21):
    a= a+ n**2
print(f"1(b) a_20 = {a}")

# c
a= 1
for n in range(1,21):
    a= 1/(1+a)
print(f"1(c) a_20 = {a:.5f}")

# d
a= 1
for n in range(1,21):
    a= np. sqrt(a+1)
print(f"1(d) a_20 = {a:.5f}")

# ==========================================
# Task 2: Functions, Sums, and Integrals
# ==========================================

# a %%%%%%%%%%%%%
f = lambda x,y: x*y - 2/x
x_pts = np.array([1,2,3])
y_pts =np.array([2,3,4])
vals = f(x_pts , y_pts)
print(f"2(a) Function values {vals}")

# b %%%%%%%%%%%

k = np.arange(0,11)
terms = (1/3)**k
geo_sum =np.sum(terms)

# verification (1-x^n)/(1-n)
geom_sum_formula = (1-(1/3)**11)/(1-1/3)
print(f"2(b) Vectorized Sum: {geo_sum:.8f}, Formula Verification: {geom_sum_formula:.8f}")

# c %%%%%%%%%%%
integral1_val = quad(lambda x: x**2, 0, 1)[0]
integral2_val = quad(lambda x: np.exp(-x), 0, np.inf)[0]

print(f"2(c) Integral of x^2 from 0 to 1: {integral1_val:.6f}")
print(f"2(c) Integral of e^(-x) from 0 to inf: {integral2_val:.6f}")


# ==========================================
# Task 3: Trapezoidal Rule Error Analysis
# ==========================================

exact_val = np.sin(1)

for n in [20 , 40 , 60 , 80 , 100]:
    x = np.linspace(0,1,n+1)
    y = np.cos(x)
    dx = x[1:] - x[:-1]
    
    s_n = np.sum(dx * (y[1:] + y[:-1])/2)
    error = np. abs(exact_val - s_n)
    print(f"Task 3: n = {n:3d} | Trapezoidal Sum = {s_n:.8f} | Absolute Error = {error:.2e}")



# ==========================================
# Task 4: Least Squares Regression & Plotting
# ==========================================

# (a) 
x = np.array([-10, -17, -4, -7, -5, -6, -11])
y = np.array([105, 163, 43, 69, 48, 56, 115])
n = len(x)

# (c) 
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_xx = np.sum(x**2)

S_xy = sum_xy - (1 / n) * sum_x * sum_y
S_xx = sum_xx - (1 / n) * (sum_x**2)

x_mean = np.mean(x)
y_mean = np.mean(y)

a = S_xy / S_xx
b = y_mean - a * x_mean

print(f"\nTask 4: Least Squares Line: y = {a:.4f}x + {b:.4f}")

# (b) & (d) 

x_line = np.linspace(min(x) - 1, max(x) + 1, 100)
y_line = a * x_line + b

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ro', label="Data points")
plt.plot(x_line, y_line, 'b-', label=f"Fit: y = {a:.2f}x + {b:.2f}")

plt.grid(True)
plt.xlabel("Last week's median temperature (°C)")
plt.ylabel("Weekly slipper orders (y)")
plt.title("Weekly Slipper Orders vs. Median Temperature")
plt.legend()
plt.show()