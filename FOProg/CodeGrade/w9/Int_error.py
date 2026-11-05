def read_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number. Please try again.")