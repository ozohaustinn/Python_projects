MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

PAYMENT_METHODS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}



def is_sufficient(user_choice):
    """ Return a boolean False if resources are not sufficient"""

    for item in user_choice:
        if user_choice[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins(payment_options):
    """ Return the total payment made by the user"""
    total = 0
    for item in payment_options:
        total += int(input(f"insert {item} to process your order: ")) * payment_options[item]
    return total


def is_transaction_successful(payment_made, drink_cost):
    """
    Return True if payment made is sufficient

    """

    if drink_cost > payment_made:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        if payment_made > drink_cost:
            change = round(payment_made - drink_cost,2)
            print(f"Here is your change: {change}")

    return True

def deduct_resources(user_choice):
    for item in user_choice:
        resources[item] -= user_choice[item]








profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}76g")
        print(f"Money: ${profit}")

    else:
        if choice not in MENU.keys():
            print("Wrong input try again")
        else:
            drink = MENU[choice]
            item_check = is_sufficient(drink["ingredients"])
            if item_check:
                payment = process_coins(PAYMENT_METHODS)
                transaction_made = is_transaction_successful(payment, drink["cost"])
                if transaction_made:
                    deduct_resources(drink["ingredients"])

                print(f"Here is your {choice}. Enjoy!")


