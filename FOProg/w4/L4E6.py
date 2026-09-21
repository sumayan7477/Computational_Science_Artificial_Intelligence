# Lecture 4, Example 6
# Print the even numbers in the list

print("Lecture 4, Example 6")
list_numbers = list(range(2, 65, 3))
print("List: ", list_numbers)
print("Even numbers in the list: ")
for x in list_numbers:
    if x % 2 != 0:
        continue
    print(x, end=", ")


