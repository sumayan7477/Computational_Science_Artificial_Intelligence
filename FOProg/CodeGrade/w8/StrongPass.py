import string
import random

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation

COMB = LETTERS + DIGITS + SPECIAL

def generate_pw(char_set , length):
    random.seed(1)
    password=""
    for i in range(length):
        password+= random.choice(char_set)
    return password



    