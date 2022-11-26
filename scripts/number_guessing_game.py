"""Play a number guessing game."""

import random

def make_guess():
    while True:
        guess = input("\nEnter any whole number between 1 and 100: ")
        try:
            guess = int(guess)
            break
        except:
            print('Invalid input, please provide integer.')
            continue
    
    return guess

# Generate a random number between 1 and 101
n = random.randrange(1, 101)

# Ask the user to have a guess
guess = make_guess()

# Keep asking until the guess is right
while n != guess:
    if guess < n:
        print("Too low")
        guess = make_guess()
    elif guess > n:
        print("Too high!")
        guess = make_guess()
    else:
        break

# Tell user they guessed right
print("you guessed it right!!")
