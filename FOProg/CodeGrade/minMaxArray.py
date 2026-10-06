def get_smallest(num_list):
    min = num_list[0]
    for num in num_list:
        if float(min)>num:
            min = num
    return min
    

def get_largest(num_list):
    max = num_list[0]
    for num in num_list:
        if float(max)< num:
            max = num
    return max
