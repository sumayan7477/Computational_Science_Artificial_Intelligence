# Lecture 6 Example 3
# Iterating over a list

my_list = [1, 2, 3, 4, 5]

# Case 1 - Using for ... in
print("Case 1")
for item in my_list:
    print(item)

print("")

# Case 2 - Using in range()
print("Case 2")
for i in range(len(my_list)):
    print(my_list[i])

print("")

# Case 3 - Using while
print("Case 3")
i = 0
while i < len(my_list):
    print(my_list[i])
    i = i + 1
