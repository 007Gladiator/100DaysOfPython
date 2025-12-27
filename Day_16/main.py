from importlib.resources import is_resource

from Day_16.menu import MenuItem
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu_item = MenuItem()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    coffee_order = input(f"Please select the coffee type : {menu.get_items()}")
    if coffee_order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif coffee_order in menu.get_items():
        coffee_details = menu.find_drink(coffee_order)
        print(coffee_details)
        if coffee_details and coffee_maker.is_resource_sufficient(coffee_details):
            payment_done = money_machine.make_payment(coffee_details.cost)
            if payment_done:
                coffee_maker.make_coffee(coffee_details)
    else:
        print(f"Incorrect input, please try again.")


