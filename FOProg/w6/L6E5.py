# Lecture 6 Example 5
# Matrix examples

# List of lists = Matrix
list_of_lists = [[1,2], [3,4], [5,6]]
print("list_of_lists", list_of_lists)
print("list_of_lists[0]", list_of_lists[0])
print("list_of_lists[0][0]", list_of_lists[0][0])
print("list_of_lists[2][1]", list_of_lists[2][1])

# A case for a loop inside a loop!
for row in list_of_lists:
    for value in row:
        print(value, end=" ")
    # Line change after each row
    print("")
