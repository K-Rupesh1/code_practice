from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)#it is used to set the screen size by using width and height
user_bet=screen.textinput
user_input=screen.textinput(title="Make your bet",prompt="guess the turtle which will win? enter that turtle colour")
print(user_input)
colours=["red","pink","green","blue","black","yellow"]
y_position=[-70,-40,-10,20,50,80]

all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=timmy=Turtle()
    timmy.shape("turtle")
    timmy.color(colours[turtle_index])
    timmy.penup()
    timmy.goto(x=-230,y=y_position[turtle_index]) #goto is used for directions 
    all_turtles.append(new_turtle)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
    for timmy in (all_turtles):
        if timmy.xcor()>230:  #x co-ordinate greather than 230
            is_race_on = False
            winning_color=timmy.pencolor()
            if user_input==winning_color:
                print(f"you won !your winning colour is {winning_color}")
            else:
                print(f"you lost!the winning colour is {winning_color}")
                break
        turtle_distance=random.randint(0,10)
        timmy.forward(turtle_distance)
screen.exitonclick()
