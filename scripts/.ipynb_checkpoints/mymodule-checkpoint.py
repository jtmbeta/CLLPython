"""mymodule"""

import random


def guess_the_number():
    """Play a number guessing game
    
    Returns
    -------
    None
    """
    
    # Generate a random number between 1 and 101
    number = random.randrange(1, 101)
    
    print("Let's play a guessing game!\n")
    
    # Ask the user to have a guess
    guess = int(float(input("Enter any whole number between 1 and 100: ")))

    # Keep asking until the guess is right
    while number != guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > number:
            print("Too high!")
            guess = int(input("Enter number again: "))
        else:
            break

    # Tell user they guessed right
    print("You guessed it right!!\n")
    
    # Return the number
    return number

def check_prime_number(number):
    """Check if a number is prime.
    
    Parameters
    ----------
    number : int
        The number to check (must be an integer).
        
    Returns
    -------
    is_prime : bool
        Whether `number` is a prime number.
    
    """
    
    # Throw an error if number is not an integer
    if not isinstance(number, int):
        raise ValueError(
            f"check_prime_number expects int, not {type(number)}"
        )
        
    # Define a flag variable
    is_prime = False

    # Prime numbers are greater than 1
    if number > 1:
        # Check for factors
        for i in range(2, number):
            print("Testing for " + str(i))
            if (number % i) == 0:
                # If factor is found, set flag to True
                is_prime = True
                # Break out of loop
                break
        
    return is_prime

def fahrenheit_to_celsius(temp):
    """Convert Fahrenheit to Celsius.
    
    Parameters
    ----------
    temp : int or float
        Temperature in Fahrenheit.
        
    Returns
    -------
    celsius : float
        Equivalent temperature in Celsius.
        
    """

    # Throw an error if number is not integer or floating point
    if not isinstance(temp, (int, float)):
        raise ValueError(
            f"fahrenheit_to_celsius expects int or float, not {type(temp)}"
        )
        
    # Convert to Celsius
    celsius = (temp - 32) * (5 / 9)
    celsius = round(celsius, 2)
    
    # Return the temperature
    return celsius
