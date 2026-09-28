def print_menu():
    """ Print the menu options for calculation"""
    print("1) an addition")
    print("2) a substraction")
    print("3) a multiplication")
    print("4) a division")
    print("0) Quit")
    return int(input("Enter your choice:"))

def ask_numbers():
    num1 = int(input("give the first number:"))
    num2 = int (input("give the second number:"))
    return(num1,num2)

def addition(num1 , num2):
    return num1 + num2   
def sudstitution(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def Division(num1, num2):
    return round(num1 / num2 , 2)
 
#  main program
while True:
    choice = print_menu()
    
    if choice == 1:
        numbers = ask_numbers()
        print(f"{numbers[0]} +{numbers[1]} = {addition(numbers[0],numbers[1])}")
    elif choice == 2:
        numbers = ask_numbers()
        print(f"{numbers[0]} -{numbers[1]} = {sudstitution(numbers[0],numbers[1])}")
    elif choice == 3:
        numbers = ask_numbers()
        print(f"{numbers[0]} * {numbers[1]} = {multiplication(numbers[0],numbers[1])}")
    elif choice == 4:
        numbers = ask_numbers()
        if numbers[1]==0:
            print("Error: Division is zero")
        else:
            print(f"{numbers[0]} / {numbers[1]} = {Division(numbers[0],numbers[1])}")
    
    elif choice==0:
        print("Bye")
        break
    else:
        print("Invalid choise")