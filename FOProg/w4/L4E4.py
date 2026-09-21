# Lecture 4, Example 4
# Example of a while loop

print("Lecture 4, Example 4")

# Initialize the score to be nothing
score = ""
while (score != "-1"):
    # Ask the user input at the start
    score = input("Please input score OR -1 to quit: ")
    if (score == "-1"):
        print("Bye!")
    elif float(score) >= 50:
        print("Pass")
    else:
        print("Reject")



