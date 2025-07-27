from turtle import Turtle,Screen
import random
colours=["red", "green", "blue","orange", "purple","pink","violet", "cyan", "turquoise","black","brown", "beige", "tan"]
timmy=Turtle()
timmy.speed("fastest")
angle=0
for i in range(0,75):
    timmy.color(random.choice(colours))
    timmy.circle(100)
    #timmy.setheading(timmy.heading()+10)#heading() is used for knowing the present position of a timmy
    timmy.setheading(angle)
    angle+=5


screen=Screen()
screen.exitonclick()