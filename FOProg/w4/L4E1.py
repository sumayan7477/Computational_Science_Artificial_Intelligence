# Lecture 4, Example 1
# Combine the capital letters of each word in the sentence
# e.g. Central Processing Unit => CPU

print("Lecture 4, Example 1")
print("Combine the capital letters of each word in the sentence")

sentence = input("Enter a sentence with capital letters: ")
print("The capital letters of ", sentence, "are: ")
for character in sentence:
    # If the character is uppercase
    if character.isupper():
        # Print the uppercase character
        print(character, end="")


