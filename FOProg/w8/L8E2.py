import math

# Example of using pi to calculate the circumference of a circle
radius = 5
circumference = 2 * math.pi * radius
print("Circumference of a circle with radius 5:", circumference)

# Flooring values
number = 5.9
print("The floor of 5.9 is:", math.floor(number))

# Ceiling values
number = 5.1
print("The ceiling of 5.1 is:", math.ceil(number))


# Example: calculate the future value of an investment with continuous compounding
principal = 1000  # Initial amount in dollars
rate = 0.05       # Annual interest rate of 5%
time = 3          # Time in years

# Calculate future value with continuous compounding
future_value = principal * math.exp(rate * time)
print("Future value of the investment after 3 years:", future_value)
