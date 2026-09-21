# Lecture 4, Example 3
# Examples of for loop with range() function

print("Lecture 4, Example 3")
# printing the results in sequence 1+2+3+4+...+100
seq_sum = 0
for i in range(1, 100+1):
    seq_sum = seq_sum + i
print("1 + 2 + 3 + 4 + ... + 100 =", seq_sum)

# printing the results for sequence 11*9*7*...*3*1
seq_mul = 1
for i in range(11, 0, -2):
    seq_mul = seq_mul * i
print("11 * 9 * 7 * ... * 1 =", seq_mul)





