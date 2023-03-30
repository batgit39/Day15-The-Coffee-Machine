import os
from art import logo
from Data import menu, resources 
profit = 0

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕️. Enjoy!\n")


def resource_checker(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.\n")
            return False
    return True

def process_payment():
    print("Please insert your coins : ")
    total = int( input("how many quarters?: ")) * 0.25
    total += int( input("how many dimes?: ")) * 0.1
    total += int( input("how many nickles?: ")) * 0.05
    total += int( input("how many pennies?: ")) * 0.01
    return total

def transaction_checker(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.\n")
        return False

os.system('clear')
coffee = True
while coffee:
    print(logo)
    user = input("​What would you like?(Please enter full name)\n1. espresso\n2. latte\n3. cappuccino : ")
    os.system('clear')
    if user == "turn-off":
        coffee = False
    elif user == "report-data":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money(total profit): ${profit}")
    elif user == "latte" or user == "espresso" or user == "cappuccino" :
        drink = menu[user]
        if resource_checker(drink["ingredients"]):
            payment = process_payment()
            if transaction_checker(payment, drink["cost"]):
                make_coffee(user, drink["ingredients"])
    else:
        print("Wrong input. Please Try again.")
