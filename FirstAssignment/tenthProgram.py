# Write a program that takes three inputs (first name, last name, and birth year), stores them in variables, and prints: "Your full name is [first] [last], and you are [age] years old."

first_name = input("Enter Your First Name:")
last_name = input("Enter Your Last Name:")
birth_year = input("Enter Your Birth Year:")

age = 2025 - int(birth_year)

print(f"Your full name is {first_name} {last_name}, and you are {age} years old.")