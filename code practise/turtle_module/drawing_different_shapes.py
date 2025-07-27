from turtle import Turtle,Screen
import random 

"""#print without using a function
colour=["red","green","yellow","blue"]

timmy=Turtle()
a=random.choice(colour)

for i in range(4):
    
    timmy.color(a)
    timmy.forward(100)
    timmy.right(90)
    b=random.choice(colour)
for i in range (5):
    
    timmy.color(b)
    timmy.forward(100)
    timmy.right(72)
c=random.choice(colour)
for i in range(8):
    
    timmy.color(c)
    timmy.forward(100)
    timmy.right(45)"""


#by using a function
timmy=Turtle()
colours=["red", "green", "blue","orange", "purple","pink","violet", "cyan", "turquoise","black","brown", "beige", "tan"]

def draw_shape (number_of_sides):
    
    angle=360/number_of_sides
    for i in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)
for shapes in range(3,11):
    timmy.color(random.choice(colours))
    draw_shape(shapes)
    


screen=Screen()
screen.exitonclick()