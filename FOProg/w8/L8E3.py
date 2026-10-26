import random

# Generate a random even number between 0 and 10
even_number = random.randrange(0, 11, 2)
print("Random even number between 0 and 10:", even_number)

# Generate a random integer between 1 and 6 (like rolling a die)
die_roll = random.randint(1, 6)
print("Random integer between 1 and 6:", die_roll)

# Randomly choose a fruit from the list
fruits = ["apple", "banana", "cherry", "date"]
chosen_fruit = random.choice(fruits)
print("Randomly chosen fruit:", chosen_fruit)
