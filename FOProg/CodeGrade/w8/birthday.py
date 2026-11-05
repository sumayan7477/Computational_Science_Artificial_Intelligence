from datetime import datetime

def read_date(prompt):
    text= input(prompt)
    return datetime.strptime(text , "%d/%m/%Y")

def birthday_this_year(birthday , today):
    return birthday.replace(year = today.year)

def print_birthday_status(today , birthday):
    current_birthday = birthday_this_year(birthday , today)

    if current_birthday.date() == today.date():
        print("The birthday is today !")
    elif current_birthday < today:
        days = (today - current_birthday).days
        print(f"The birthday passed {days} days ago.")
    else:
        days = (current_birthday - today).days
        print(f"The birthday will be in {days} days.")
def main():
    today = read_date("Enter today's date (dd/mm/yyyy):\n")
    birthday = read_date("Enter the birthday (dd/mm/yyyy):\n")
    print_birthday_status(today , birthday)

#main()