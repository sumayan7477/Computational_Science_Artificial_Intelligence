# Chapter 9, Example 1

while True:
    try:
        nr = int(input("Enter an integer: "))
        break
    except:
        print("You did not give an integer, retry!")

print(f"The entered integer is {nr}")
