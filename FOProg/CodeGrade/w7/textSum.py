def sum_num_file(path):
    file = open(path , 'r')
    numbers_array = file.readlines()
    file.close()

    Total=0
    for number in numbers_array:
        Total= Total+ float(number.strip())
    return Total
