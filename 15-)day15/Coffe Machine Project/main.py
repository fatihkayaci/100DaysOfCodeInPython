import os
from db import MENU, resources
#TODO: Print report: when the user enters "report" to the prompt, shows the current resource values.
def report():
    for key, value in resources.items():
        print(f"{key.title()}: {value}ml")
    
    coffe_details = input("Do you want detailed information about making coffee? 'yes' or 'no' ")
    if coffe_details.lower() == "yes":
        for drink, info in MENU.items():
            print(f"{drink.title()} (${info['cost']}):")
            for ingredient, amount in info["ingredients"].items():
                print(f"  {ingredient.title()}: {amount}ml")
            print()
            
#TODO: Check resources sufficient: the program warning if not enough resource for make coffee. it is say "Sorry there is not enough water".
def check_resources_sufficient(user_choice):
    ingredients = MENU[user_choice]['ingredients']
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return
    print("yours coffee is making")
    process_coins(user_choice)
    
#TODO: Process coins: if there are sufficient resources to make the drink selected. insert coins.       
def process_coins(user_choice):
    print("Please insert coins.")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    result = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    cost = MENU[user_choice]['cost']
    if result <cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        #TODO: Check transaction successful
        print(f"Here is ${result - cost: 06.2f} in change.")
        print(f"Here is your {user_choice}. Enjoy!")
        update_resources()

def update_resources():
    for item in MENU[user_choice]['ingredients']:
        resources[item] = resources[item] - MENU[user_choice]['ingredients'][item]
        
def coffe_machine():
    if user_choice == "report":
        report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        check_resources_sufficient(user_choice)
        
continue_progress = True
while continue_progress:
    #TODO: The program will ask the user "What would you like? (espresso/latte/cappuccino):"
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    #TODO: For maintainers of the coffee machine, they can use "off"
    if user_choice == "off":
        continue_progress = False
    else:
        coffe_machine()
        