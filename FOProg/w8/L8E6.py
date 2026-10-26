from datetime import datetime

## HOW TO WRITE DIFFERENT TIME STRINGS?

# Get today's date and time
now = datetime.now()

# Format the date in different ways
formatted_date1 = now.strftime("%Y-%m-%d")        # Year-Month-Day
formatted_date2 = now.strftime("%d/%m/%Y")        # Day/Month/Year
formatted_date3 = now.strftime("%B %d, %Y")       # Full month name, Day, Year
formatted_date4 = now.strftime("%I:%M %p")        # Hour:Minute AM/PM

print("Formatted date (YYYY-MM-DD):", formatted_date1)
print("Formatted date (DD/MM/YYYY):", formatted_date2)
print("Formatted date (Month DD, YYYY):", formatted_date3)
print("Formatted time (HH:MM AM/PM):", formatted_date4)

## HOW TO READ DIFFERENT DATE STRINGS?

# Example date strings
date_string1 = "2024-10-27"
date_string2 = "27/10/2024 14:30"
date_string3 = "October 27, 2024"

# Convert date strings to datetime objects
date1 = datetime.strptime(date_string1, "%Y-%m-%d")
date2 = datetime.strptime(date_string2, "%d/%m/%Y %H:%M")
date3 = datetime.strptime(date_string3, "%B %d, %Y")

print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)
