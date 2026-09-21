# Lecture 4, Example 7
# Nested loop - Multiplication table

print("Lecture 4, Example 7")
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i) + "*" + str(j) + "=" + str(i*j), end="\t")
    # Row change after each i change
    print()



