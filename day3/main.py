# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride")
#     age = int(input("What is your age "))
#     if 12 >= age or age <= 18:
#         print("Child tickets are $7")
#         bill = 7
#     elif age < 12:
#         print("Youth tickets are $5")
#         bill = 5
#     elif age >= 45 and age <= 55:
#         print("Free ride! becuase you are old")
#     else:
#         print("Adult tickets are $12")
#         bill = 12

#     wants_photo = input("Do  you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Total cost would be {bill}")

# else:
#     print("You cant ride")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure")
first_step = input(
    "You enter the cave and there are roads which one you choose, left or right?").lower()
second_step = "No choosen"
third_step = "No choosen"
if first_step == "left":
    second_step = input(
        "You keep making your way into the cave, there is a boat that looks a bit fragile, you take the boat or swing?").lower()
    if second_step == "boat":
        third_step = input(
            "After navigating in the boat you foudn 3 doords with these colors: Red, Yellow, Blue").lower()
        if third_step == "Red":
            print("Sadly you got burned by fire. Game Over")
        elif third_step == "Yellow":
            print("You won!!")
        elif third_step == "Blue":
            print("You got Eaten by beasts. Game Over!")
        else:
            print("Wrong choice game over!")
    else:
        print("You got Attacked by trout. Game Over!")
else:
    print("Fall into a hole. Game Over.")
