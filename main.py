from utils import square, is_even, celsius_to_fahrenheit, greet

# Ask the user for a number
user_input = input("Enter a number: ")
number = float(user_input)

# Do the math using our tools from utils.py
sq = square(number)
even = is_even(number)
fahr = celsius_to_fahrenheit(number)

# Print out the results clearly
print("Square:", sq)
print("Is it even?", even)
print("Fahrenheit:", fahr)
print(greet("student"))