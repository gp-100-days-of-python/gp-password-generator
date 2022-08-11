#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Producing a random password but keeping the letter, symbol and number order
pw_letters = ""
for letter in range(0, nr_letters):
    pw_letters += letters[random.randint(0, 25)]

pw_symbols = ""
for symbol in range(0, nr_symbols):
    pw_symbols += symbols[random.randint(0, 8)]

pw_numbers = ""
for number in range(0, nr_numbers):
    pw_numbers += numbers[random.randint(0, 9)]

random_password = pw_letters + pw_symbols + pw_numbers

print(random_password)

# Shuffling the produced password to randomize it further

# Method-1: just to random sample the string
shuffled_password = ''.join(random.sample(random_password, len(random_password)))

print(shuffled_password)

# Method-2: convert the string to a list and use shuffle function to shuffle the list

random_password_as_list = list(random_password)
random.shuffle(random_password_as_list)
shuffled_password_using_shuffle = ''.join(random_password_as_list)

print(shuffled_password_using_shuffle)
