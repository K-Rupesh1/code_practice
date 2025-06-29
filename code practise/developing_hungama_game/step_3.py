import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

correct=[]
gameover=False
while not gameover:
    guess=input("guess a letter" ).lower
    display=""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display += letter
        else:
            display += "_"
    print(display)