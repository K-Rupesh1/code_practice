#it is developed by using hints
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score. Returns 0 for a Blackjack, otherwise the sum."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer scores and returns the result message."""
    if user_score == computer_score:
        return "It's a draw."
    elif user_score == 0:
        return "User wins with a Blackjack!"
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score > 21:
        return "User went over. User loses."
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

# Initialize the cards
user_cards = []
computer_cards = []

# Deal 2 cards each
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

game_over = False

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True

# Computer draws cards until score is 17 or more
while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"\nYour final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))
