# print("Hello"[len("Hello") - 1])

# num_char = len(input("What is your name?"))

# new_num_char = str(num_char)

# Summing two strings numbers
# print("Your name has " + new_num_char + " characters.")
# two_digit_number = input("Type a two digit number. ")

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# print(int(first_digit) + int(second_digit))


# BMI calculator

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# BMI = int(weight) / (float(height) ** 2)
# print(BMI)7

# score = 0
# height = 1.8
# isWinning = True
# # f-String

# print(f"your score is {score}")

# years of life
# age = input("What is your current age? ")
# remaining_age = 90 - int(age)
# months = remaining_age * 12
# weeks = remaining_age * 52
# days = remaining_age * 365

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print("Welcome to the tip calculator.")
bill_cost = input("What was the total bill? $")
percentage_tip = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_cost_as_float = float(bill_cost)

total_bill = bill_cost_as_float + \
    (bill_cost_as_float * (int(percentage_tip) / 100))

total_pay_per_person = total_bill / int(people)

total_pay_per_person_rounded = round(total_pay_per_person, 2)

final_amount = "{:.2f}".format(total_pay_per_person)

print(f"Each person should pay: {final_amount}")
