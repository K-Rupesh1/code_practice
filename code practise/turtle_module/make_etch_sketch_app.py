import turtle
timmy=turtle.Turtle()
screen=turtle.Screen()
def move_forward():
    timmy.forward(30)
def move_right():
    angle=timmy.heading()+10
    timmy.setheading(angle)
def move_left():
    angle=timmy.heading()-10
    print(angle)
    timmy.setheading(angle)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown


screen.listen() # it is used for to read the input by user
screen.onkey(move_forward,"space")
screen.onkey(move_right,"r")
screen.onkey(move_left,"l")
screen.onkey(clear,"c")

screen=screen.exitonclick()