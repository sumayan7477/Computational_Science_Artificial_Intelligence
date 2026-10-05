# Lecture 6 Example 4
# Input + Lists

def input_integers():
    input_string = input("Give integers separated by comma:\n")
    print(input_string)
    list_of_chars = input_string.split(",")
    print(list_of_chars)

    list_of_ints = []
    for char in list_of_chars:
        list_of_ints.append(int(char))

    return list_of_ints


# TESTING
output = input_integers()
print(output)
