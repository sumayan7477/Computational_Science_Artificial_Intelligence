a = True
b = False
print("a and b:", a and b)  # False
print("a and True:", a and True)  # True

# Example of 'or' operator
print("a or b:", a or b)  # True
print("b or False:", b or False)  # False

# Example of 'not' operator
print("not a:", not a)  # False
print("not False:", not False)  # True

# Boolean operators can be also combined (use parethesis!)
age = 25
is_student = True
has_member_card = False

if (age >= 18 and is_student) or has_member_card:
    print("Eligible for concert ticket discount")
else:
    print("Not eligible for concert ticket discount")
