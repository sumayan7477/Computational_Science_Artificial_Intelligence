 # Join two strings together -- no space is added
word1 = "Hello"
word2 = "World"
word3 = word1 + word2
print(word3 + "\n") # Added a newline in the end

# To add a space between them, add a " ":
word1 = "Hello"
word2 = "World"
word3 = word1 + " " + word2
print(word3 + "\n")


# If you try to combine a string and a number, Python will give you an error
number = 5
word = "Stars"
#combination = number + word # comment this out

# You need to convert the number into a string
combination = str(number) + word
print(combination)
 

