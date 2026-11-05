import random

def generate_number():
    random.seed(6)
    num = random.randint(0,100)
    return num
def get_guess():
    return int(input("Guess the number:\n"))

def check_guess(guess , secret):
    if guess < secret:
        print("The number is larger.")
        return False
    elif guess> secret:
        print("The number is smaller.")
        return False
    else:
        return True
def main():
    secret = generate_number()
    guesses = 0

    while True:
        guess = get_guess()
        guesses +=1

        if check_guess(guess , secret):
            print("Congratulations! You guessed the number.")
            print("Number of guesses:" , guesses)
            break
#main()