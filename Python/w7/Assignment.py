import numpy as np
import matplotlib.pyplot as plt

print("==============================================")
print("TASK 1: Systems of Equations")
print("==============================================")

# (a) Form coefficient matrices A and right-hand side constant vectors b
A1 = np.array([[1, 1, -4], 
               [2, -1, 2], 
               [2, 1, 2]], dtype=float)
b1 = np.array([-2, 0, -6], dtype=float)

A2 = np.array([[0, 1, -4], 
               [2, 0, 2], 
               [2, 2, -6]], dtype=float)
b2 = np.array([-3, 0, -5], dtype=float)

A3 = np.array([[0, 1, -4], 
               [2, 0, 2], 
               [2, 2, -6]], dtype=float)
b3 = np.array([-3, 0, -6], dtype=float)

A4 = np.array([[3, 0, -1, 0], 
               [0, 2, -2, -1], 
               [8, 0, 0, -2]], dtype=float)
b4 = np.array([0, 0, 0], dtype=float)

# (b) Calculate determinants for (i) - (iii)
det1 = np.linalg.det(A1)
det2 = np.linalg.det(A2)
det3 = np.linalg.det(A3)
print(f"Determinant (i): {det1:.4f}")
print(f"Determinant (ii): {det2:.4f}")
print(f"Determinant (iii): {det3:.4f}")

# (c) Solve systems with unique solutions using np.linalg.solve
x_solve_1 = np.linalg.solve(A1, b1)
x_solve_2 = np.linalg.solve(A2, b2)
print("\nSolution using np.linalg.solve:")
print(f"System (i): {x_solve_1}")
print(f"System (ii): {x_solve_2}")

# (d) Solve using inverse matrix: x = inv(A) @ b
x_inv_1 = np.linalg.inv(A1) @ b1
x_inv_2 = np.linalg.inv(A2) @ b2
print("\nSolution using inverse matrix (inv(A) @ b):")
print(f"System (i): {x_inv_1}")
print(f"System (ii): {x_inv_2}")


print("\n==============================================")
print("TASK 2: Message Encryption")
print("==============================================")

# Encryption matrix
A_enc = np.array([[1, 1, 0], 
                  [0, 1, 0], 
                  [0, 1, 1]])

# (a) Message "erase the files" encoded into 3 x 5 matrix
# e=5, r=18, a=1, s=19, e=5, space=0, t=20, h=8, e=5, space=0, f=6, i=9, l=12, e=5, s=19
msg_matrix = np.array([
    [5, 19, 20, 0, 12],
    [18, 5, 8, 6, 5],
    [1, 0, 5, 9, 19]
])

encrypted_msg = A_enc @ msg_matrix
print("Encrypted Message Matrix:\n", encrypted_msg)

# (b) Decryption demonstration
inv_A_enc = np.linalg.inv(A_enc)
decrypted_matrix = np.round(inv_A_enc @ encrypted_msg).astype(int)
print("Decrypted Message Matrix:\n", decrypted_matrix)


print("\n==============================================")
print("TASK 3: Dice Roll Simulation 1")
print("==============================================")

# (a) Define random variable die [1, 6]
die = np.random.randint(1, 7)

# (b) Roll the die 10 times
rolls_10 = np.random.randint(1, 7, size=10)
threes_10 = np.sum(rolls_10 == 3)
print(f"10 Rolls: {rolls_10}")
print(f"Number of threes in 10 rolls: {threes_10}")

# (c) Roll the die 234 times
rolls_234 = np.random.randint(1, 7, size=234)
count_3 = np.sum(rolls_234 == 3)
count_4 = np.sum(rolls_234 == 4)
print(f"234 Rolls -> Threes: {count_3} ({count_3/234*100:.2f}%), Fours: {count_4} ({count_4/234*100:.2f}%)")

# (d) Plot histogram for 234 rolls
plt.figure(figsize=(8, 4))
plt.hist(rolls_234, bins=np.arange(0.5, 7.5, 1), edgecolor='black')
plt.title("Histogram of 234 Dice Rolls")
plt.xlabel("Outcome")
plt.ylabel("Frequency")
plt.xticks(range(1, 7))

# (e) Roll the die 60,000 times and plot histogram with density
rolls_60k = np.random.randint(1, 7, size=60000)
plt.figure(figsize=(8, 4))
plt.hist(rolls_60k, bins=np.arange(0.5, 7.5, 1), density=True, edgecolor='black', alpha=0.7)
plt.axhline(y=1/6, color='r', linestyle='--', label='Theoretical Probability (1/6)')
plt.title("Histogram of 60,000 Dice Rolls (Density)")
plt.xlabel("Outcome")
plt.ylabel("Relative Frequency")
plt.xticks(range(1, 7))
plt.legend()
plt.show()


print("\n==============================================")
print("TASK 4: Dice Roll Simulation 2")
print("==============================================")

# (a) Estimate probability that sum is 3 using 1 million rolls
n_simulations = 1000000
die1 = np.random.randint(1, 7, size=n_simulations)
die2 = np.random.randint(1, 7, size=n_simulations)
sums = die1 + die2

prob_sum_3 = np.mean(sums == 3)
print(f"Estimated Probability (Sum = 3): {prob_sum_3:.5f}")
print(f"Theoretical Probability (2/36): {2/36:.5f}")

# (b) Plot histogram of sums showing probabilities
plt.figure(figsize=(8, 4))
plt.hist(sums, bins=np.arange(1.5, 13.5, 1), density=True, edgecolor='black', align='mid', alpha=0.7)
plt.title("Probability Distribution of Sums of Two Dice")
plt.xlabel("Sum of Two Dice")
plt.ylabel("Probability")
plt.xticks(range(2, 13))
plt.show()
