# Week 10 - Example 3
# Original dictionary with a nested list
person = {
    "name": "John",
    "age": 30,
    "city": ["Helsinki", "Tallinn"]
}

# Shallow copy using the dictionary's copy() method
shallow_copied_person = person.copy()

# Modify the first city in the shallow copy
shallow_copied_person["city"][0] = "Stockholm"

# Print both dictionaries to observe the changes
print("Original person:", person)
print("Shallow copied person:", shallow_copied_person)

# To manually create a "deep copy" without importing, we can duplicate the nested structures
deep_copied_person = {
    "name": person["name"],
    "age": person["age"],
    "city": person["city"][:]
}

# Modify the first city in the "deep copy"
deep_copied_person["city"][0] = "Oslo"

# Print all dictionaries to observe the difference
print("\nAfter manual deep copy modification:")
print("Original person:", person)
print("Deep copied person:", deep_copied_person)
