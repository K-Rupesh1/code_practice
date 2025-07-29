
import turtle
import random
timmy=turtle.Turtle()
#turtle.colormode(255)
#colors_list=[(226, 231, 236)
"""(58, 106, 148)
(224, 200, 109)
(134, 84, 58)
(223, 138, 62)
(196, 145, 171)
(234, 226, 204)
(224, 234, 230)
(141, 178, 204)
(139, 82, 105)
(209, 90, 69)
(188, 80, 120)
(68, 105, 90)
(237, 225, 233)
(134, 182, 136)
(133, 133, 74)
(63, 156, 92)
(48, 156, 194)
(183, 192, 201)
(214, 177, 191)
(19, 57, 93)
(21, 68, 113)
(112, 123, 149)
(229, 174, 165)
(172, 203, 182)
(158, 205, 215)
(69, 58, 47)
(108, 47, 60)
(53, 70, 65)
(72, 64, 53)
(134, 42, 38)
(47, 66, 61)
(0, 122, 125)]"""
colors_list=["red","pink","green","blue","black"]
number_of_dots=100
timmy.penup()
timmy.hideturtle()
for i in range(1,number_of_dots):
    color=random.choice(colors_list)
    timmy.shape("turtle")
    timmy.dot(10,color)
    timmy.forward(25)
    
    if i%10==0:
        timmy.setheading(90)
        timmy.forward(20)
        timmy.setheading(180)
        timmy.forward(250)
        timmy.setheading(0)

    
screen=turtle.Screen()
screen.exitonclick()
