from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def get_user_choice(available_drinks):
    return input(f"What would you like?: {available_drinks}: ").lower()


def main():
    machine = MoneyMachine()
    coffee_machine = CoffeeMaker()
    menu = Menu()
    is_machine_on = True
    while is_machine_on:
        user_choice = (get_user_choice(menu.get_items()))
        drink = menu.find_drink(user_choice)
        if user_choice == "off":
            exit()
        if user_choice == "report":
            coffee_machine.report()
            machine.report()
            continue

        if not drink:
            continue

        if coffee_machine.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


main()
