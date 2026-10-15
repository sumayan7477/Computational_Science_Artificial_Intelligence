file = open('people.csv', 'r') # Open the CSV file
lines = file.readlines() # Read the file content
file.close() # you can close the file already now

data = [] # An empty list to store the data

# Process each line
for line in lines:
    row = line.strip().split(',')  # !!!
    data.append(row)

# We have a matrix of strings

print(data)
print()

# Rows correspond to the first index

for i in range(len(data)):
    print(data[i])

print()

# Print data of person Eva

for i in range(len(data)):
    if data[i][0] == "Eva":
        print("Name:",data[i][0],"Age:",data[i][1],"Address:",data[i][2])
