import random
import string

print("Welcome to the Password Generator!")
length = int(input("How many characters would you like in your password? "))

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Input validation for the number of letters, symbols, and numbers
while True:
    try:
        nr_lowercase = int(input("How many lowercase letters would you like? "))
        nr_uppercase = int(input("How many uppercase letters would you like? "))
        nr_digits = int(input("How many digits would you like? "))
        nr_symbols = int(input("How many symbols would you like? "))
        if nr_lowercase + nr_uppercase + nr_digits + nr_symbols != length:
            raise ValueError("The sum of the requested characters does not match the password length.")
        break
    except ValueError as e:
        print(e)

password_list = []

# Generate password
for _ in range(nr_lowercase):
    password_list.append(random.choice(lowercase_letters))

for _ in range(nr_uppercase):
    password_list.append(random.choice(uppercase_letters))

for _ in range(nr_digits):
    password_list.append(random.choice(digits))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle and join the password list
random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")