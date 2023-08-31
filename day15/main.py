# Coffee Machine
from data import resources, coins_value, MENU

possible_choices = ["report", "latte", "cappuccino", "expresso"]


def print_resorces(water, milk, coffee, money):
    print(
        f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}ml\nMoney: ${money}")


def get_user_choice():
    return input(
        f"What would you like?: {possible_choices[1]}/{possible_choices[2]}/{possible_choices[3]}: ").lower()


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
    has_machine_resources = True
    while has_machine_resources:
        selected_choice = get_user_choice()
        while selected_choice not in possible_choices:
            print("Select a valid option")
            selected_choice = get_user_choice()

        if selected_choice == possible_choices[0]:
            print_resorces(water, milk, coffee, money)

        if selected_choice == possible_choices[1]:
            inserted_money = get_coins()
            latte_cost = MENU["latte"]["cost"]
            changed = inserted_money - latte_cost
            money += latte_cost
            print(f"Here is ${round(changed, 2)} in change")


main()
