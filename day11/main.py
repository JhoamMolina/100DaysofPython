import random
import os
from art import logo
############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

cards_len = len(cards)
players_cards = []
machine_cards = []
play_game = "y"


def get_card_from_deck(deck):
    card = random.choice(deck)
    return card


def sum_current_cards(cards):
    sum_of_cards = 0
    for card in cards:
        sum_of_cards += card

    return sum_of_cards


def computer_final_hand(cards):
    sum = sum_current_cards(cards)
    print(
        f"Computer's final hand: {cards}, final score: {sum}")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_player_cards(cards):
    sum = sum_current_cards(cards)
    print(f"Your cards: {cards}, current score {sum}")


while play_game == "y":
    play_game = input(
        "Do you want to play a game Blackjack? Type 'y' or 'n': ").lower()

    if play_game == "y":

        clear_console()
        players_cards = []
        machine_cards = []
        print(logo)

        players_cards.append(get_card_from_deck(cards))
        players_cards.append(get_card_from_deck(cards))
        player_cards_sum = players_cards[0] + players_cards[1]

        machine_cards.append(get_card_from_deck(cards))

        show_player_cards(players_cards)
        print(f"Computer's first card: {sum_current_cards(machine_cards)}")

        one_more_card = "y"

        while one_more_card == "y":
            one_more_card = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if one_more_card == "y":
                new_card = get_card_from_deck(cards)
                if new_card == 11 and ((11 + sum_current_cards(players_cards)) > 21):
                    players_cards.append(1)
                else:
                    players_cards.append(new_card)

                if sum_current_cards(players_cards) > 21:
                    show_player_cards(players_cards)
                    print(
                        f"Computer's first card: {sum_current_cards(machine_cards)}")
                    print("You went over. You Lose 😭")
                    one_more_card = "n"
                else:
                    show_player_cards(players_cards)
                    print(
                        f"Computer's first card: {sum_current_cards(machine_cards)}")

            else:
                while sum_current_cards(machine_cards) < 17:
                    machine_cards.append(get_card_from_deck(cards))

                if sum_current_cards(machine_cards) > 21:
                    show_player_cards(players_cards)
                    computer_final_hand(machine_cards)
                    print("You won!")
                elif sum_current_cards(players_cards) > sum_current_cards(machine_cards):
                    show_player_cards(players_cards)
                    computer_final_hand(machine_cards)
                    print("You won!")
                    one_more_card = "n"

                elif sum_current_cards(players_cards) < sum_current_cards(machine_cards):
                    show_player_cards(players_cards)
                    computer_final_hand(machine_cards)
                    print("You Lose!")
                    one_more_card = "n"

                else:
                    show_player_cards(players_cards)
                    computer_final_hand(machine_cards)
                    print("It's a draw! 😒")
                    one_more_card = "n"
