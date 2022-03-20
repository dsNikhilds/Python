from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_obj = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()


repeat = True

while repeat:
    user = input(f"What would you like? {menu_obj.get_items()}:\n").lower()
  #  print(menu_obj.find_drink(user))
    if user == "off":
        repeat = False
        
    elif user == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
        
    else:
        drink = menu_obj.find_drink(user)
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
        