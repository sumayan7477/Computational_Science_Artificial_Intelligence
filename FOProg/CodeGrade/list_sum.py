def list_sum(num_list):
    sum = 0
    for num in num_list :
        sum = sum + float(num)

    return sum

list_test = [73, 12, 95, 41, -8, 27, 66, 30, -89, 54]
print("The sum of elements in the list is:", list_sum(list_test))
