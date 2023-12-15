from art import logo1, logo2
from menu import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIME = 0.10
NICKEl = 0.05
PENNY = 0.01
money = 0


def report():
    """prints a report on resources available"""
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource}: {resources[resource]}ml")
        else:
            print(f"{resource}: {resources[resource]}g")
    print(f"Money: ${money}")


def deal(coffee, coins):
    """
    :param coffee: str(name of coffee)
    :param coins: int(amount)
    :return: profit or False
    """
    cost = MENU[coffee]["cost"]
    if coins < cost:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        profit = cost
        change = round(coins - cost, 2)
        for ingredient in MENU[coffee]["ingredients"]:
            resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        print(f"Here is your {coffee} Enjoy!")
    return profit


def ask_money():
    """ Take in coins and calculates it"""
    print("insert coins")
    quarter = int(input("quarter: "))
    dime = int(input("dime: "))
    nickel = int(input("nickel: "))
    penny = int(input("penny: "))
    return quarter * QUARTER + dime * DIME + nickel * NICKEl + penny * PENNY


def needs_resources(coffee):
    """
    :param coffee: str(name of coffee)
    :return: list of resources or False
    """
    needed_resources = []
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
            needed_resources.append(ingredient)
    if needed_resources:
        return needed_resources
    else:
        return False


print(logo1, logo2)

def coffee_machine():
    """
    A coffee Machine, makes a coffee and runs in a loop.
    """
    coffee_decision = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_decision == "off":
        return
    elif coffee_decision == "report":
        report()
    else:
        resources_needed = needs_resources(coffee_decision)
        if not resources_needed:
            coins = ask_money()
            global money
            money += deal(coffee_decision, coins)
        else:
            for resource in resources_needed:
                print(f"Sorry, there is not enough {resource}")
    coffee_machine()


coffee_machine()