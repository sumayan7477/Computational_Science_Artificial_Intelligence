def divide(a, b):
    if b != 0:
        return a / b
#    else:             # These two lines can be removed! Why?
#        return None

#result = divide(10, 2)
result = divide(10, 0) #Try with this!

if result is None:
    print("Error: Division by zero!")
else:
    print(result)
