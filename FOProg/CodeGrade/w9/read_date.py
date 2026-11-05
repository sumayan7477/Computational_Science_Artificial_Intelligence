from datetime import datetime

def read_date(prompt):
    while True:
        try:
            date = input(prompt)
            return datetime.strptime(date , "%d/%m/%Y")
        except ValueError:
            print("Invalid date. Please use the format dd/mm/yyyy.")

