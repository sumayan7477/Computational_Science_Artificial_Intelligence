def modify_parameter(my_list):
    my_list[2] = 33  # This modifies the third element
    A = my_list      # A refers to the same memory location as my_list
    A[0] = 1000      # This will change also my_list

# Before the function
original_list = [1, 2, 3]
print("Before:", original_list)

# After the function
modify_parameter(original_list)
print("After:", original_list)
