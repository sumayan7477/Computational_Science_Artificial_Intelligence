def remove_duplicates(num_list):
    list =[]
    for num in num_list:
        if list.count(num)==0:
            list.append(num)
    return list
