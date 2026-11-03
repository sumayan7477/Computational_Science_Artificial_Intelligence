# This example divides 10 by a number

while True:
    try:
        x = int(input("Enter an integer: "))
        y = 10 / x
        print(y)
        break   # all went good
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except ZeroDivisionError:
        print("Division by zero error. Give other number than zero.")
    except KeyboardInterrupt:
        print("User interrupted the program.")
        break  # Optional: Exit the while loop
 
