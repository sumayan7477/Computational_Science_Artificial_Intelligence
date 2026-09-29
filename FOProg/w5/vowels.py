def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count


# Example usage:
text = "Hello World"
result = count_vowels(text)
print(f"Number of vowels: {result}")  