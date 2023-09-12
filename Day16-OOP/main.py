from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

    if coffee_maker.is_resource_sufficient(drink) == True and money_machine.make_payment(drink.cost) == True:
        coffee_maker.make_coffee(drink)
        
    