# Week 10 - Example 4
import csv

# Open the CSV file (no "with" statement for file handling)
csvfile = open("csv_e04.csv")

# Create a DictReader object to read each row as a dictionary
reader = csv.DictReader(csvfile)

# Loop through each row in the CSV file
for row in reader:
    # Print the values for 'name', 'age', and 'gender' from each row
    print(row["name"], row["age"], row["gender"])

# Close the CSV file after reading
csvfile.close()
