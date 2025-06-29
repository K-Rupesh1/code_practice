print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice=input("enter you the way you want to move left or right")
if choice=="left":
    print("you moved to another step.. ")
    choice1=input("if you want to swim or wait")
    if choice1=="wait":
        print("you moved to another step")
        choice2=input("which door you want to open red , blue,yellow")
        if choice2=="red":
            print("burned by fire gameover")
        elif choice2=="yellow":
            print("you win")
        elif choice2=="blue":
            print("eaten by beasts gameover")
        else:
            print("game over")
    else:
        print("attacked by trout game over")
else:
    print("fall into a hole game over")