# Coffee Machine
from data import resources, coins_value, MENU

possible_choices = ["report", "latte", "cappuccino", "espresso", "off"]


def print_resorces(water, milk, coffee, money):
    print(
        f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")


def get_user_choice():
    choices_str = "/".join(possible_choices[1:4])
    return input(f"What would you like?: {choices_str}: ").lower()


def check_resources(water, milk, coffee, type_of_coffee):
    water -= MENU[type_of_coffee]["ingredients"]["water"]
    milk -= MENU[type_of_coffee]["ingredients"]["milk"]
    coffee -= MENU[type_of_coffee]["ingredients"]["coffee"]
    is_out_of_resources = False
    if water < 0:
        print("Sorry there is not enough water.")
        is_out_of_resources = True
    if milk < 0:
        print("Sorry there is not enough milk.")
        is_out_of_resources = True
    if coffee < 0:
        print("Sorry there is not enough coffee.")
        is_out_of_resources = True
    return is_out_of_resources, water, milk, coffee


def is_money_enough(inserted_money, type_of_coffe: str):
    if inserted_money < MENU[type_of_coffe]["cost"]:
        print("Sorry that's not enought money. Moeny refunded.")
        return False
    return True


def print_change(inserted_money, type_of_coffee: str):
    change = inserted_money - MENU[type_of_coffee]["cost"]
    print(f"Here is ${round(change, 2)} in change")
    return change


def print_coffee_to_user(type_of_coffee: str):
    print(f"Here is your {type_of_coffee} ☕")


def get_coins():
    print("Please insert Coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    coins_sum = quarters * \
        coins_value["quarter"] + dimes * coins_value["dime"] + \
        nickles * coins_value["nickel"] + pennies * coins_value["penny"]

    return coins_sum


def main():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    is_machine_on = True
    while is_machine_on:
        selected_choice = get_user_choice()
        while selected_choice not in possible_choices:
            print("Select a valid option")
            selected_choice = get_user_choice()

        if selected_choice == possible_choices[0]:
            print_resorces(water, milk, coffee, money)
            continue

        if selected_choice == possible_choices[4]:
            is_machine_on = False
            continue

        inserted_money = get_coins()
        if not is_money_enough(inserted_money, selected_choice):
            continue
        is_out_of_resources, water, milk, coffee = check_resources(
            water, milk, coffee, selected_choice)
        if is_out_of_resources:
            continue
        money += MENU[selected_choice]["cost"]
        print_change(inserted_money, selected_choice)
        print_coffee_to_user(selected_choice)


main()
