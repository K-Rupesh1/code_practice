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
profit=0
orders=["espresso","latte","cappuccino"]
def coffee_type(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    print("please insert a coins")
    quarters =int(input("enter a quarters"))* 0.25
    dimes = int(input("enter a dimes"))*0.10
    nickles =int(input("enter a nickles"))*0.05
    pennies =int(input("enter a pennnies"))*0.01
    total=quarters+dimes+nickles+pennies
    return total
def check_money(money_received,drink_cost):
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"your change :{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffe(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"your drink name is {drink_name}.enjoy")
is_on =True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if coffee_type(drink["ingredients"]):
            payment = process_coins()
            if check_money(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])