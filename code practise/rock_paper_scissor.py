import random
rock=''
paper=''
scissor=''
game_image=[rock,paper,scissor]
user_input=int(input("enter 0 for rock\n enter 1 for pepper\n enter 2 for scissors"))
if user_input>=0 and user_input<=2:
    print(game_image[user_input])

computer_choice=random.randint(0,2)
print(game_image[computer_choice])
if user_input == computer_choice:
    print("match draw")
elif user_input > computer_choice:
    print("you lose")
else:
    print("you win")