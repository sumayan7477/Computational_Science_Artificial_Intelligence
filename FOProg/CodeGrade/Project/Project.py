# Car rental management system
#my approach is , creating small functions so that it would be easier to debug other wise main functions become heavy.
from datetime import datetime , timedelta

#define file name to use whenever needed

VEHICLES_FILE = "vehicles.txt"
CUSTOMERS_FILE = "customers.txt"
RENTED_FILE = "rentedVehicles.txt"
TRANSACTIONS_FILE = "transactions.txt"
DATE_FORMAT = "%d/%m/%Y"
DATETIME_FORMAT = "%d/%m/%Y %H:%M"

#Read a file

def read_rows(filename):
    data = []
    try:
        file = open(filename ,"r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("The file" + filename + "was not found.")
        return data
    for line in lines:
        line = line.strip()
        if line !="":
            row = line.split(",")
            data.append(row)
    return data

#Turn list into line
def row_to_line(row):
    line = row[0]
    for i in range(1,len(row)):
        line = line + "," +row[i]
    return line + "\n"

#Append one row to the end of a file.
def append_row(filename , row):
    file = open(filename , "a")
    file.write(row_to_line(row))
    file.close()

#overwrite a file
def write_rows(filename , data):
    file = open(filename, "w")
    for row in data:
        file.write(row_to_line(row))
    file.close()

#Findind data________

# car info based on plate data
def find_vehicle(plate):
    for row in read_rows(VEHICLES_FILE):
        if row[0] == plate:
            return row
    return  None

#row of open rental
def find_rental(plate):
    for row in read_rows(RENTED_FILE):
        if row[0]== plate:
            return row
    return None

# customer  based on date of birth
def find_customer(birthdate):
    for row in read_rows(CUSTOMERS_FILE):
        if row[0] == birthdate:
            return row
    return None

#functions for velidation__________

#current date time
def now_as_text():
    return datetime.now().strftime(DATETIME_FORMAT)

#Turn string into date
def parse_birthdate(text):
    if len(text) != 10 or text[2] != "/" or text[5] !="/":
        return None
    try:
        return datetime.strptime(text , DATE_FORMAT)
    except ValueError:
        return None

#Compute a persions age .
def age_today(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year
    if today.month < birthdate.month:
        age = age-1
    elif today.month == birthdate.month and today.day < birthdate.day:
        age = age -1
    return age

#if text contain a comma or space
def has_comma_or_space(text):
    for character in text:
        if character == "," or character == " ":
            return True
    return False

# a name must start with a capital letter
def is_valid_name(name):
    if name == "" or has_comma_or_space(name):
        return False
    return name[0].isupper()

#An email should contain @ and a .
def is_valid_email(email):
    if has_comma_or_space(email):
        return False
    found_at = False
    found_dot_after_at = False
    for character in email:
        if character == "@":
            found_at = True
        elif character == "." and found_at:
            found_dot_after_at = True
    return found_at and found_dot_after_at

#counting rental period
def rental_days(start , end):
    days = 1
    while start + timedelta(days = days) <end:
        days = days + 1
    return days

# money conversions
def cents_to_text(cents):
    euros = int(cents / 100)
    rest = cents % 100
    if rest < 10:
        return str(euros) + ".0" +str(rest)
    return str(euros) + "." + str(rest)

# operations____________

# Print cars can be rented

def list_available_cars():
    print("The following cars are available:")
    count = 0
    for row in read_rows(VEHICLES_FILE):
        if len(row) >= 4 and find_rental(row[0]) is None:
            print("* Reg. nbr : " + row[0] + ", Model: " + row[1] +", Price per day :" + row[2])
            
            #Everything from position 4 onwards is a property  so i am making a list of those properties
            properties = row[3]
            for i in range(4 , len(row)):
                properties = properties + ", " + row[i]
            print(" Properties: "  + properties)
            count = count + 1
    if count == 0:
        print("(no cars available at the moment)")

# rent a car
def rent_car():

    #first take a input nbr and check if this car is available
    
    plate = input("Give the register number of the car you want to rent: ").strip()

    if find_vehicle(plate) is None:
        print("There is no car with the number")
        return
    if find_rental(plate) is not None:
        print("The car is already rented.")
        return

    #if avaiable then take birthdate of user and calculate age
    
    birthdate_text = input("Please enter your birthdate in the form DD/MM/YYYY: ").strip()
    birthdate = parse_birthdate(birthdate_text)
    if birthdate is None:
        print("Invalid date. Use the from DD/MM/YYYY.")
        return
    age = age_today(birthdate)
    if age < 18 or age > 100:
        print("Sorry, customer must be between 18 and 100 years old.")
        return
    
    #check if the customar exist or not
    
    customer = find_customer(birthdate_text)
    if customer is None:
        print("Welcome! you are a new customer.")
        
        first_name = input("Enter your First name: ").strip()
        if not is_valid_name(first_name):
            print("Invalid first name , It must start with a capital letter.")
            return

        last_name = input("Enter your last name: ").strip()
        if not is_valid_name(last_name):
            print("Invalid last name, It must start with a capital letter.")
            return
        email = input("Please enter your email address: ").strip()
        if not is_valid_email(email):
            print("Invalid email adress.")
            return

        append_row(CUSTOMERS_FILE, [birthdate_text, first_name, last_name, email])
    else:
        first_name = customer[1]

# after renting add a new row in rented car list

    append_row(RENTED_FILE,[plate, birthdate_text, now_as_text()])
    print("Hello " + first_name)
    print("You rented the car " + plate)



#returning a car
def return_car():

    #take reg number as input to find out if the car is renteed
    
    plate = input("Give the register number of the car you want to return: ").strip()

    rental = find_rental(plate)
    if rental is None:
        print("The car is not currently rented.")
        return
    #check if the car in the list
    
    vehicle = find_vehicle(plate)
    if vehicle is None:
        print("The car is not in the vehicle list . ")
        return
    
    # if propertiec are lless then three info cannot be processed
    if len(rental)< 3 or len(vehicle)<3:
        print("The date for this rental is broken and cannot be processed.")
        return
    try:
        start = datetime.strptime(rental[2] , DATETIME_FORMAT)
        daily_rate = int(vehicle[2])
    except ValueError:
        print("The data for this rental is broken and cannot be peocessed.")
        return

    #calculating rental period and count total cost
    
    end_text = now_as_text()
    end = datetime.strptime(end_text , DATETIME_FORMAT)
    days = rental_days(start , end)
    price_text = cents_to_text(days* daily_rate * 100)
    
    # remove the car from list
    remaining = []
    for row in read_rows(RENTED_FILE):
        if row[0] != plate:
            remaining.append(row)
    write_rows(RENTED_FILE, remaining)

    # record it in transactions
    append_row(TRANSACTIONS_FILE,[plate, rental[1], rental[2], end_text, str(days), price_text])
    print("The rent lasted " + str(days) + "days and the cost is " + price_text + "euros")
    
            
#Count money
def count_money():
    total_cents = 0
    for row in read_rows(TRANSACTIONS_FILE):
        if len(row)<6:
            print("Skipping a broken row in " + TRANSACTIONS_FILES)
            continue
        try:
            total_cents = total_cents + round(float(row[5])*100)
        except ValueError:
            print("Skipping a broken row in " + TRANSACTIONS_FILES)
    print("The total amount of money is " + cents_to_text(total_cents) + "euros")

#menu for options

def show_menu():
    print()
    print("Select one")
    print("1. List of available cars")
    print("2. Rent a car ")
    print("3. return a car")
    print("4. Count the money")
    print("0. Exit")
    return input("What is your selection?").strip()

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            list_available_cars()
        elif choice == "2":
            rent_car()
        elif choice == "3":
            return_car()
        elif choice == "4":
            count_money()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose 1,2,3,4 or 0.")

if __name__ == "__main__":
   main()

        
        
    
    

        































