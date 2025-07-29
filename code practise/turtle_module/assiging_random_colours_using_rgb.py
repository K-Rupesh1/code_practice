
import turtle
import random
screen=turtle.Screen()
screen.colormode(255)
timmy=turtle.Turtle()
timmy.pensize(10)
angle=[90,180,270]

def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
   
    return(r,g,b)

for i in range(0,200):
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(angle))


screen.exitonclick()

