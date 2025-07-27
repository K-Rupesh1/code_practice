from turtle import Turtle,Screen
import random
timmy=Turtle()
colours=["red", "green", "blue","orange", "purple","pink","violet", "cyan", "turquoise","black","brown", "beige", "tan"]
state=["forward","back"]
position=["left","right"]


def walk(no_of_walks):
    for i in range(1,50):
        timmy.color(random.choice(colours))#it will generates the random colour for every turn
        direction=random.choice(state)
        turn=random.choice(position)
        getattr(timmy,direction)(50)
        getattr(timmy,turn)(90)


walk(5)

"""def walk(no_of_walks):
    for i in range(1,50):
        
        direction=random.choice(state)
        turn=random.choice(position)
        getattr(timmy,direction)(50)
        getattr(timmy,turn)(90)
for i in range(1,5):
    timmy.color(random.choice(colours))#it will generates the random colour after function runs one time 
    walk(5)"""
"""angle=[90,180,270]
timmy.pensize(10)#it will choose the size of the pen i,e.thickness of the line
timmy.speed("normal")
for i in range(0,200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(angle))#setheading is used for choose the direction of a timmy,not a left and right
    """



screen=Screen()
screen.exitonclick()
