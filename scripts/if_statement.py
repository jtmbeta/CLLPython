"""Some Boolean logic."""

# Some Boolean expressions.
world_is_round = True
world_is_flat = False
sugar_is_sweet = True
is_saturday = False
is_sunday = True
is_weekday = False
on_holiday = False

# Some variables
price_of_first_class_stamp = 0.95
money_in_pocket = 1.20

# Simple if statement
if world_is_round:
    print("The world is round.")

# If statement with logical 'and' to compare boolean expressions
if world_is_round and sugar_is_sweet:
    print("The world is round and sugar is sweet.")

# If statement with logical 'not' to compare boolean expressions
if not world_is_flat:
    print("The world is not flat.")

# If/elif/else statement with logical 'or' to compare boolean expressions
if is_saturday or is_sunday:
    print("Don't go to work.")
elif is_weekday:
    print("Go to work.")
else:
    print("What planet are you living on?")

# If statement with >= (greater-or-equals) to compare numerical values
if money_in_pocket >= price_of_first_class_stamp:
    print("Buy first class stamp")
    # Update value with -= (minus-equals) assignment oprator
    money_in_pocket -= price_of_first_class_stamp
    print(f"£{money_in_pocket} left in pocket")
