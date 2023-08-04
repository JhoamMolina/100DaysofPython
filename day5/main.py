# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
letters_len = int(input("How many letters would you like in your password?\n"))
symbols_len = int(input("How many symbols would you like?\n"))
numbers_len = int(input("How many numbers would you like?\n"))


whole_array = [letters, numbers, symbols]
amount_array = [letters_len, symbols_len, numbers_len]

# password_len = int(letters_len) + int(symbols_len) + int(numbers_len)
# new_password = ""

# for n in range(password_len):
#     characters = whole_array
#     amount_array_update = amount_array
#     x = random.randint(0, len(characters) - 1)
#     selected_array = characters[x]
#     if amount_array_update[x] != 0:
#         new_password += selected_array[random.randint(
#             0, len(selected_array) - 1)]
#         amount_array_update[x] -= 1
#     else:
#         del characters[x]
#         del amount_array_update[x]
#         x = random.randint(0, len(characters) - 1)
#         selected_array = characters[x]
#         if amount_array_update[x] != 0:
#             new_password += selected_array[random.randint(
#                 0, len(selected_array) - 1)]
#             amount_array_update[x] -= 1
#         else:
#             del characters[x]
#             del amount_array_update[x]
#             new_password += characters[0][random.randint(
#                 0, len(characters[0]) - 1)]
#             print(amount_array_update)
#             amount_array_update[0] -= 1

# random_letters = []
# random_symbols = []
# random_numbers = []
# new_password = ""

# for letter in range(0, letters_len):
#     letter = letters[random.randint(0, 51)]
#     random_letters.append(letter)

# for number in range(0, numbers_len):
#     number = numbers[random.randint(0, 9)]
#     random_numbers.append(number)

# for symbol in range(0, symbols_len):
#     symbol = symbols[random.randint(0, 8)]
#     random_symbols.append(symbol)

# random_letters += random_symbols
# random_letters += random_numbers
# for char in range(len(random_letters)):
#     x = random.randint(0, len(random_letters) - 1)
#     new_password += random_letters[x]
#     del random_letters[x]


# chatgpt solution

random_letters = [letters[random.randint(0, 51)] for _ in range(letters_len)]
random_numbers = [numbers[random.randint(0, 9)] for _ in range(numbers_len)]
random_symbols = [symbols[random.randint(0, 8)] for _ in range(symbols_len)]

all_chars = random_letters + random_symbols + random_numbers
random.shuffle(all_chars)

new_password = "".join(all_chars)


print(f"Here is your password: {new_password}")
