"""Check if a number is prime."""

# Take input from the user
num = int(input("Enter a number: "))

# Define a flag variable
flag = False

# Prime numbers are greater than 1
if num > 1:
    # Check for factors
    for i in range(2, num):
        print("Testing for " + str(i))
        if (num % i) == 0:
            # If factor is found, set flag to True
            flag = True
            # Break out of loop
            break

# Check if flag is True
if flag:
    print(num, "is not a prime number.")
else:
    print(num, "is a prime number.")
