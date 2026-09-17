import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.special import factorial


# 1(a)

def f(x):
    return 1/(x**2 +1)

x_values = np.linspace(0,4,200)
y_values =f(x_values)

plt.figure()
plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = 1/(x^2 + 1)")
plt.grid(True)
plt.show()

# 1(b)
f_b = lambda x : 1 /(x + 0.5)**2 + x
y_values_b = f_b(x_values)

plt.figure()
plt.plot(x_values, y_values_b)
plt.xlabel("x")
plt.ylabel("f_b(x)")
plt.title("Plot of f_b(x) = 1/(x + 0.5)^2 + x")
plt.grid(True)
plt.show()


# 2(a)

f_eq =lambda x: x**2 -4

# using fsolve to find the root of the equation
root1 = fsolve(f_eq, x0=1.0)[0]
root2 = fsolve(f_eq, x0=-1.0)[0]
print(f"fsolve Root 1: {root1}")
print(f"fsolve Root 2: {root2}")
print("-" * 40)


# unsing numpy's roots function to find the roots of the polynomial
poly_roots = np.roots([1, 0, -4])
print(f"Polynomial Roots: {poly_roots}")
print("-" * 40)

# 2(b) system of equations

def system(v):
    x, y = v
    return[
        y - x + 1,
        y + x - 1
    ]
# initial guess
v0 = [0.0, 0.0]

sol = fsolve(system, v0)
print(f"fsolve Solution: {sol}")
print("-" * 40)

# 3(a)
k_a = np.arange(0 , 21)
val_a =np.sum( 1/factorial(k_a))
print(f"Sum of series for k=0 to 20: {val_a}")

# 3(b)
k_b = np.arange(1,6)
val_b = np.prod(k_b**2)
print(f"Product of squares for k=1 to 5: {val_b}")

# 3(c)
k_c = np.arange(1,61)
val_c = 500* np.sum(1+k_c/12)
print(f"Sum for k=1 to 60: {val_c}")

# 3(d)
k_d = np.arange(1,61)
val_d = 500 * np.sum(1.03**(k_d/12))
print(f"Sum for k=1 to 60: {val_d}")

print("-" * 40)

# 4
def p(n):
    """Computes the BBP approximation of pi for a given n."""
    k = np.arange(0, n + 1)
    
    # Calculate each term of the series
    term = (1 / 16**k) * (
        4 / (8*k + 1) - 
        2 / (8*k + 4) - 
        1 / (8*k + 5) - 
        1 / (8*k + 6)
    )
    
    return np.sum(term)

print("4: Errors |pi - p(n)| for n = 0, ..., 6:")

for n in range(7):
    p_n = p(n)
    error = np.abs(np.pi - p_n)
    print(f"n = {n}: p(n) = {p_n:.14f} | Error = {error:.2e}")