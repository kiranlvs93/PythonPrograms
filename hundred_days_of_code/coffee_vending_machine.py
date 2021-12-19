# Make 3 hot flavours - espresso/latte/cappuccino. Every type needs different ingredients
# Coffee machine resources - Max - 300 ml water/200ml milk/100g coffee
# Coin operated - {"penny":1, "dime":10, "nickel": 5, "quarter": 25}
# Requirements in the file ../input/Coffee+Machine+Program+Requirements.pdf
# Commands:
# 1. off - Turn off the machine
# 2. report - Report on the resources left

menu = {
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
coins = {"quarter": 0.25, "dime": 0.1, "nickel": 0.05, "penny": 0.01}
resources = {"water": 300, "milk": 200, "coffee": 100}

income = 0


def get_report():
    """
    Get the report of the current income and ingredients left
    :return:
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${income}")


def get_coins():
    """
    Ask user for denomination of the each coin and convert it into dollars
    :return:
    """
    coins_value = 0
    print("Please insert coins.")
    for coin, value in coins.items():
        coins_value += int(input(f"How many {coin}s?:")) * value
    print(f"You have paid ${round(coins_value, 2)}.")
    return coins_value


def make_coffee(order):
    """
    Reduce the resources based on the coffee type
    Serve the coffee HOT :-)
    :param order: User choice
    :return:
    """
    ingredients = menu[order]["ingredients"]
    for item, volume in ingredients.items():
        resources[item] -= volume
    print(f"Here is your {order} ☕ Enjoy!")


def is_resource_sufficient(order_ingredients):
    """
    Returns True when order can be made, False if ingredients are insufficient.
    :param order_ingredients:
    :return:
    """
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(order):
    """
    If there are enough resources for preparing the order, get coins from user.
    If the user has paid more than the order value, hand him over the change.
    :param order:
    :return:
    """
    global income
    ingredients = menu[order]['ingredients']
    if is_resource_sufficient(ingredients):
        payment_by_customer = get_coins()
        order_value = menu[order]["cost"]
        if payment_by_customer < order_value:
            print("Sorry that's not enough money. Money refunded.")
            return False
        if payment_by_customer > order_value:
            print(f"Here is ${round(payment_by_customer - order_value, 2)} in change.")
        income += order_value
        return True
    else:
        return False


def get_user_choice():
    """
    Get user input until its valid.
    :return:
    """
    try:
        user_input = input("What would you like? 1.espresso($1.5) 2.latte($2.5) 3.cappuccino($3.0)?").lower()
        user_input = "espresso" if user_input == "1" else "latte" if user_input == "2" else "cappuccino" if user_input == "3" else user_input
        if user_input not in ["espresso", "latte", "cappuccino", "report", "off"]:
            print("Invalid input. Please try again.")
            return get_user_choice()
        return user_input
    except Exception as e:
        print(f"Invalid input. Please try again. Exception {e}")
        return get_user_choice()


def start_brewing():
    user_input = get_user_choice()
    if user_input == "report":
        get_report()
    elif user_input == "off":
        print("Machine Turned Off. Resources status::")
        get_report()
        exit()
    else:
        if is_transaction_successful(user_input):
            make_coffee(user_input)
    start_brewing()


start_brewing()
