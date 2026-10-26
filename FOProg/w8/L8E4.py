# Set a seed to ensure reproducible random values
random.seed(42)

# Generate a few random values
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
fruit = random.choice(["apple", "banana", "cherry", "date"])

print("Random number 1:", number1)
print("Random number 2:", number2)
print("Randomly chosen fruit:", fruit)
