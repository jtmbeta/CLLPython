"""Convert Fahrenheit to Celsius."""

# Ask user to enter a temperature in Fahrenheit
temp = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (temp - 32) * (5 / 9)
celsius = round(celsius, 2)

print(f"{temp} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
