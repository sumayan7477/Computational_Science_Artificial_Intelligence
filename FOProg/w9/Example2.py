
while True:
    try:
        number = int(input("Give an integer: "))
        print("You gave", number)
        break
    
    except Exception as e:
        print(type(e))  # the class of error
        print(e)        # prints the message
        print("Please retry!")



