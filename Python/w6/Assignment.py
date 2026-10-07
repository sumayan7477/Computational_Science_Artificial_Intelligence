import numpy as np
# -----------------------------------
# task 1
# -----------------------------------
# a
A = np.array([[1 ,2, 3, 4, 5, 6,7,8],[9, 11, 13, 15, 17, 19, 21,23]])
print("1(a) matrix A is: \n",A)

# b
# A_transpose = A.T
A_transpose = np.transpose(A)
print("\n1(b) matrix A transpose is: \n",A_transpose)

# c


# d
A_d = np.array([[3, 2], [3, 5]])
B_d = np.array([[4, 3], [1, 2]])
x_d = np.array([[4], [1]])

A_plus_BT = A_d + B_d.T
 # Matrix multiplication
AB = A_d @ B_d       
BA = B_d @ A_d
Ax = A_d @ x_d

print("\n1(d) A + B^T:\n", A_plus_BT)
print("AB:\n", AB)
print("BA:\n", BA)
print("Ax:\n", Ax)

# (e) Solve system of equations Ax = b
# System:
#  1x + 0y + 1z = 1
#  2x - 2y + 1z = 0
#  1x + 2y + 1z = 2
A_eq = np.array([
    [1,  0, 1],
    [2, -2, 1],
    [1,  2, 1]
])
b_eq = np.array([1, 0, 2])

x_sol = np.linalg.solve(A_eq, b_eq)
print("\n1(e) Solution x [x, y, z]:\n", x_sol)

#%% -----------------------------------
# task 2
# -----------------------------------
import numpy as np

# (a) 
ones_mat = np.ones((3, 4))
zeros_mat = np.zeros((2, 5))
eye_mat = np.eye(4)

# (b) Random vectors and matrices
# (iii) Generate vector of 10 numbers in range (0, 5)
# Formula: (b - a) * rand + a  =>  5 * rand + 0
vec_0_5 = 5 * np.random.rand(10)

# Generate 3x4 matrix in range (-2, 2)
# Formula: (2 - (-2)) * rand + (-2) = 4 * rand - 2
mat_neg2_2 = 4 * np.random.rand(3, 4) - 2

print("2(b) Vector (0, 5):\n", vec_0_5)
print("2(b) Matrix (-2, 2):\n", mat_neg2_2)

# (c) Rounding comparison
rand_mat = mat_neg2_2

print("\n2(c) original matrix:\n", rand_mat)
print("np.round:\n", np.round(rand_mat))  # Rounds to nearest integer
print("np.floor:\n", np.floor(rand_mat))  # Rounds DOWN to nearest integer
print("np.ceil:\n", np.ceil(rand_mat))    # Rounds UP to nearest integer

#%% -----------------------------------
# task 3
# -----------------------------------
import numpy as np

# (a) Compare matrix operations
A = np.array([
    [1/3, 2/3],
    [1/2, 1/2]
])

print("3(a) A @ A @ A (Matrix multiplication A^3):\n", A @ A @ A)
print("np.linalg.matrix_power(A, 3):\n", np.linalg.matrix_power(A, 3))
print("A**3 (Element-wise exponentiation):\n", A**3)


# (b) Powers of matrix A
print("\n3(b) A^5:\n", np.linalg.matrix_power(A, 5))
print("A^10:\n", np.linalg.matrix_power(A, 10))
print("A^100:\n", np.linalg.matrix_power(A, 100))

# gives the stationary distribution. Rows become identical
# The matrix has converged to its limit if Values don't change between $A^{10}$ and $A^{100}$.

# (c) Butterfly population dynamics
# State vector: [Meadow A caterpillars, Meadow A butterflies, Meadow B caterpillars, Meadow B butterflies]
M = np.array([
    [0,    30, 0,  5],
    [0.03, 0,  0,  0],
    [0,    10, 0,  20],
    [0,    0,  0.01, 0]
])

pop = np.array([600, 15, 300, 12])

# Simulate for 50 years to observe long-term behavior
for year in range(1, 51):
    pop = M @ pop

print("\n3(c) Population after 50 years:\n", pop)

#%% -----------------------------------
# task 4
# -----------------------------------

import numpy as np

N = 99

# (a) Assemble 99x99 tridiagonal matrix A
main_diag = 2 * np.ones(N)
sub_super_diag = -1 * np.ones(N - 1)

A = np.diag(main_diag, 0) + np.diag(sub_super_diag, 1) + np.diag(sub_super_diag, -1)

# (b) Create alternating RHS vector b: [1, -1, 1, -1, ..., 1]
b = np.array([1 if i % 2 == 0 else -1 for i in range(N)])

# (c) Solve Ax = b
x = np.linalg.solve(A, b)

print("4(c) Solution vector x (first 10 elements):\n", x[:10])
print("\nUnique values in x (rounded):\n", np.unique(np.round(x, 5)))