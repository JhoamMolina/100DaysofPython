from art import logo, vs
from game_data import data
from random import choice


def print_a_choice(instagram_profile, A_or_B):
    name = instagram_profile["name"]
    description = instagram_profile["description"]
    country = instagram_profile["country"]
    if (A_or_B == "Compare"):
        print(
            f"Compare {A_or_B}: {name}, a {description}, from {country}")
    else:
        print(
            f"Against {A_or_B}: {name}, a {description}, from {country}")


def compare_function(choice1, choice2):
    return choice1["follower_count"] > choice2["follower_count"]


def print_versus_info(first_choice, second_choice):
    print_a_choice(first_choice, "A")
    print(vs)
    print_a_choice(second_choice, "B")


def main():
    score = 0
    first_choice = choice(data)
    second_choice = choice(data)
    # Ensure first_choice and second_choice are different
    while first_choice == second_choice:
        second_choice = choice(data)

    game_over = False
    while not game_over:
        print_versus_info(first_choice, second_choice)
        user_choice = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == "a":
            user_choice = first_choice
            other_choice = second_choice
        else:
            user_choice = second_choice
            other_choice = first_choice

        if compare_function(user_choice, other_choice):
            score += 1
            print(f"You are right, score: {score}")
            first_choice = user_choice
            second_choice = choice(data)
            while first_choice == second_choice:
                second_choice = choice(data)
        else:
            print("you lose")
            game_over = True


if __name__ == "__main__":
    print(logo)
    main()
