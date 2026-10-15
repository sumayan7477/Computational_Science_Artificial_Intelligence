file = open('people.csv', 'r') # Open the CSV file
lines = file.readlines() # Read the file content
file.close() # you can close the file already now

data = [] # An empty list to store the data

# Process each line
for line in lines:
    row = line.strip().split(',')  # !!!
    data.append(row)
 

# Delete data of person Eva

for line in data: 
    if line[0] == "Eva":
        data.remove(line) # data is a list of rows!

print(data)

file = open('people.csv', 'w') # Open the file for writing 
for line in data:
    output = line[0] + "," + line[1] + "," + line[2] + "\n"
    file.write(output)
file.close()
