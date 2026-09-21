# Lecture 4, Example 5
# The loop keeps on going until number is divisible by 13
# This is done with check number % 13 == 0

print("Lecture 4, Example 5")

while True:
    n = int(input("Please enter a number: "))
    if (n % 13 == 0):
        print(n, "is divisible by 13")
        break


