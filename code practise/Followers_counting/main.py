from art import logo
from art import vs
from gamedata import data
import random
print(logo)
account_a=random.choice(data)
account_b=random.choice(data)

def format_account(account):
    account_name=account["name"]
    account_description=account["description"]
    account_country=account["country"]
    return f"{account_name},{account_description},{account_country}"
def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
score=0
game_continue=True

while game_continue:
    if account_a == account_b:
        account_b=random.choice(data)
    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")

    guess=input("enter type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    check_correct = check_answer(guess, a_follower_count, b_follower_count)
    if check_correct:
        score+=1
        print(f"your right! your current score is{score}")
    else:
        print(f"your wrong ! your score is {score}")
        game_continue=False

