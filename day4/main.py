import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.pi)

# random_float = random.random() * 5

# print(random_float)

# fruits = ["Banana", "Apple"]
# more_fruits = ["orange", "pineapple"]

# fruits.extend(more_fruits)

# print(fruits)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
possible_chocie = [rock, paper, scissors]

human_choice = input(
    "What do you choose? Typo 0 for Rock, 1 for Paper or 2 for Scissors ")

try:
    human_choice = int(human_choice)
    if human_choice not in [0, 1, 2]:
        print("Insert a valid option")
    else:
        print("Your choice")
        print(possible_chocie[human_choice])
        print("-------------------------------------------------------------")
        machine_choice = random.randint(
            0, len(possible_chocie) - 1)
        machine_draw = possible_chocie[machine_choice]
        print("Machine chooses")
        print(machine_draw)

        if human_choice == 0 and machine_choice == 2:
            print("YOU WIN!!!")
        elif human_choice == 1 and machine_choice == 0:
            print("YOU WIN!!!")
        elif human_choice == 2 and machine_choice == 1:
            print("YOU WIN!!!")
        elif human_choice == machine_choice:
            print("It's a DRAW!")
        else:
            print("YOU LOSE :(")


except ValueError:
    print("Insert a valid option")
    exit()
