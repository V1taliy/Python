import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
symbols = ['_', '!', '@', '#', '$', '%', '^', '&', '*', '(']

print("Welcome to the Password Generator!")
input_number = int(input(f"How many numbers would you like in your password?\n"))
input_letter = int(input("How many letters would you like in your password?\n"))
input_symbol = int(input("How many symbols would you like in your password?\n"))
"""
password = ""
for char in range(1, input_number + 1):
    password += random.choice(numbers)

for char in range(1, input_letter + 1):
    password += random.choice(letters)

for char in range(1, input_symbol + 1):
    password += random.choice(symbols)

print(password)
"""
#Hard level

password_list = []
for char in range(1, input_number + 1):
    password_list.append(random.choice(numbers))

for char in range(1, input_letter + 1):
    password_list.append(random.choice(letters))

for char in range(1, input_symbol + 1):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")