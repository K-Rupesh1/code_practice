import random
print("welocome to number guessing name")
print("iam thinking of a number between 1 and 100")
level=input(print("chose a level of difficulty 'easy' , 'hard' "))
number=random.randrange(100)
print(number)
def easy():
    if level=='easy':
        for i in range(10):
            print(f"you have  {10-i}attempts remaining to guess the number")
            gussed=int(input(print("enter a number")))
            if gussed>number:
                print("the number you entered is too high")
            elif gussed<number:
                print("the number you enterd is too low")
            else:
                print(f"you guess is correct:{number}")
                break
def hard():

    if level=='hard':
        for i in range(5):
            print(f"you have  {5 - i}attempts remaining to guess the number")
            gussed = int(input(print("enter a number")))
            if gussed > number:
                print("the number you entered is too high")
            elif gussed < number:
                print("the number you enterd is too low")
            else:
                print(f"you guess is correct:{number}")
                break
easy()
hard()