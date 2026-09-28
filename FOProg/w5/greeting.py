def greet(name, greeting = "Hello"):
    return greeting + ", " + name + "!"

# Calling the function with both parameters
print(greet("Alice", "Hi"))  # Output: Hi, Alice!

# Calling the function with only the required parameter
print(greet("Bob"))  # Output: Hello, Bob!
