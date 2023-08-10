from art import logo
import os
programming_dictionary = {"Bug": "Something really bad",
                          "Function": "Cool stuff that helps to program",
                          "loop": "Something that goes and goes"}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# # Adding items
# programming_dictionary["Team"] = "People that i work with"


# print(programming_dictionary)

# # create an empty dictioary
# empty_dictionary = {}

# # # wipe an existing dictioary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # edit an item in a dictrionary
# programming_dictionary["Bug"] = "Crazy stuff that happens in the dictionaries"
# print(programming_dictionary)

# loop through a dictioanry
# for key in programming_dictionary:
#     print(programming_dictionary[key])


# nesting

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"

# }

# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12},
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5}
# ]


# print(travel_log[0])

print(logo)
print("Welcome to the secret auction program.")
bidders = {}


def find_highest_bidder(bidding_record):
    higest_bidder_name = ""
    highest_bidder_bid = 0
    for bidder in bidding_record:
        bid = bidding_record[bidder]
        if bid > highest_bidder_bid:
            highest_bidder_bid = bid
            higest_bidder_name = bidder
    print(
        f"The winner is {higest_bidder_name} with a bid of ${highest_bidder_bid}")


while True:
    person_name = input("What is your name?: ").lower()
    person_bid = input("What's yoru bid?: $")
    bidders[person_name] = int(person_bid)
    add_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'").lower()
    if add_bidder == "no":
        find_highest_bidder(bidders)
        break
    clear_console()
