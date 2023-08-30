# higher Lovwer game
import random


def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def get_game_mode(easy_count: int, hard_count: int):
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_mode not in ["easy", "hard"]:
        print("Insert a valid option")
        exit()
    elif game_mode == "easy":
        return easy_count

    else:
        return hard_count


def get_guess():
    return int(input("Make a guess: "))


def check_guess(num_choice, random_number):
    if num_choice > random_number:
        return "Too high.", False
    elif num_choice < random_number:
        return "Too low.", False
    else:
        return f"You got it! 🎉🎊, The answer was {random_number}.", True


def main():
    easy_count = 10
    hard_count = 5

    welcome_message()
    attempts_remaining = get_game_mode(easy_count, hard_count)

    print(
        f"You have {attempts_remaining} attempts remaining to guess the number.")
    random_number = random.randint(1, 100)

    while attempts_remaining > 0:
        print("Guess again")
        num_choice = get_guess()
        message, is_correct = check_guess(num_choice, random_number)
        print(message)

        if is_correct:
            break

        attempts_remaining -= 1

    if attempts_remaining == 0:
        print("You've run out of guesse, you lose.")


if __name__ == "__main__":
    main()
