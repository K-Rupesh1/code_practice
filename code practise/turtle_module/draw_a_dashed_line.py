from turtle import Turtle,Screen,setposition
timmy=Turtle()
timmy.color("red")
for varaible in range(15):
    timmy.forward(10)
    timmy.penup()#moves turtle without drawing
    timmy.forward(20)
    timmy.pendown()#starts drawing

    


screen=Screen()
screen.exitonclick()