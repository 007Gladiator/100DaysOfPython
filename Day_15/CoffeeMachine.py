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

money = {
    "value": 0,
}

def generate_report():
    all_resources = {**resources, **money}
    print(f"all_resources : {all_resources}")
    for key, value in all_resources.items():
        if key in ["milk", "water"]:
            print(f"{key}: {value}ml")
        if key == "coffee":
            print(f"{key}: {value}gm")
        if key == "value":
            print(f"Money: ${value}")

def make_coffee(coffee_type):
    enough_resources = check_resources(coffee_type)
    if enough_resources:
        user_money = process_coins()
        transact(user_money, coffee_type)


def process_coins():
    quarters = int(input(f"Insert the quarters : "))
    dimes = int(input(f"Insert the dimes : "))
    nickels = int(input(f"Insert the nickels : "))
    pennies = int(input(f"Insert the pennies : "))
    return  0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies

def check_resources(coffee_type):
    for key in MENU[coffee_type]["ingredients"]:
        if not resources[key] > MENU[coffee_type]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def transact(user_money, coffee_type):
    # check if money sufficient
    if user_money > MENU[coffee_type]['cost']:
         # complete the transaction
         money['value'] += MENU[coffee_type]['cost']
         for key in MENU[coffee_type]["ingredients"]:
             resources[key] = resources[key] - MENU[coffee_type]["ingredients"][key]
         print(f"Here is your {coffee_type}. Enjoy!")
    else:
        print(f"Sorry that's not enough money.")


def coffee_machine_on():
    machine_on = True
    while machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino)")
        if user_input == "report":
            generate_report()
        elif user_input == "off":
            machine_on = False
        elif user_input in ["espresso", "latte", "cappuccino"] :
            make_coffee(coffee_type = user_input)
        else:
            print(f"Incorrect user input, Please try again.")

if __name__ == "__main__":
    coffee_machine_on()

