def read_numbers(path):
    try:
        file = open(path , "r")
        lines = file.readlines()
        file.close()

        numbers =[]

        for line in lines:
            line = line.strip()

            try:
                number = int(line)
                numbers.append(number)
            except ValueError:
                continue
            
        return numbers