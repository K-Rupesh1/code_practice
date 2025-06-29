import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from trhe word_list and assign it to a variable called chosen_word. Then print it.
for char in range(0,len(word_list)):
    choosen=random.choice(word_list)
print(choosen)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("guess a letter")
print(f"you guessed letter is:{guess}")
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for i in range (0,len(choosen)):
    if guess==choosen:
        print("right")
        break
else:
    print("wrong")