# Week 10 - Example 1
# How to use a dictionary?

# Dictionary
phone_numbers = { "Janne Parkkila": "555-492843", "Elon Musk": "555-2943483" }
print(phone_numbers["Elon Musk"]) # We get his number!

# List
names = ["Janne Parkkila", "Elon Musk"]
phone_numbers = ["555-492843", "555-2943483"]
# Loop
index = 0
for name in names:
    if name == "Elon Musk":
        print(phone_numbers[index])
    # Increment the index at the end of the loop
    index = index + 1
