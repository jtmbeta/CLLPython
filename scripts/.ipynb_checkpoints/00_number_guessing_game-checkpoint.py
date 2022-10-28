"""Play a number guessing game."""

import random


# Generate a random number between 1 and 101
n = random.randrange(1, 101)

# Ask the user to have a guess
guess = int(float(input("Enter any whole number between 1 and 100: ")))

# Keep asking until the guess is right
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break

# Tell user they guessed right
print("you guessed it right!!")
