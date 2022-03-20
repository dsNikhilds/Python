# Coffee maker machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coffee():
    print("Please insert coins")
    quarters = float(input("How many quarters?")) * 0.25
    dimes = float(input("How many dimes?")) * 0.10
    nickle = float(input("How many nickle?")) * 0.5
    pennies = float(input("How many pennies?")) * 0.1
    total = quarters + pennies + dimes + nickle

    if total > MENU[user]["cost"]:
        change = total - MENU[user]["cost"]
        print(f"Your change is {change}$\nEnjoy your {user}!")
        resources["water"] -= MENU[user]["ingredients"]["water"]
        resources["milk"] -= MENU[user]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user]["ingredients"]["coffee"]
    else:
        print("You don't have enough money")



repeat = True
while repeat:
    user = input("What would you like? (espresso/latte/cappuccino) (Type report for remaining ingredients: \n").lower()
    if user == "report":
        print(f'Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\n')
    else:
        if resources["water"] < 50 or resources["milk"] < 0 or resources["coffee"] <18:
            print("We don't have enough resources to make anything!")
            repeat = False
        elif resources["water"] < MENU[user]["ingredients"]["water"]:
            print("We don't have enough Water!")
        elif resources["milk"] < MENU[user]["ingredients"]["milk"]:
            print("We don't have enough Milk!")
        elif resources["coffee"] < MENU[user]["ingredients"]["coffee"]:
            print("We don't have enough Coffee!")
        else:
            coffee()