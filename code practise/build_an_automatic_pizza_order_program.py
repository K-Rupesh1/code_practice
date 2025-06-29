print(f"welcome to python pizza deliveries!")
pizza_size=input("enter what size of pizza do you want small or medium or large")

cost_of_small_pizza=15
cost_of_medium_pizza=20
cost_of_large_pizza=25

pepper_of_small_pizza=2
pepper_of_medium_pizza=3
pepper_of_large_pizza=3

extra_cheese=1


if pizza_size=="small":
    pepper=input("do you want papper y or n")
    if pepper=="y":
        cheese=input("if you want extra cheese y or n")
        if cheese=="y":
            print(f"you want to pay :${cost_of_small_pizza+pepper_of_small_pizza+extra_cheese}")
        else:
            print(f"your want to pay: ${cost_of_small_pizza+pepper_of_small_pizza}")
    else:
        cheese = input("if you want extra cheese y or n")
        if cheese == "y":
            print(f"you want to pay:${cost_of_small_pizza + extra_cheese}")
        else:
            print(f"your bill is{cost_of_small_pizza}")
elif pizza_size=="medium":
    pepper=input("do you want papper y or n")
    if pepper=="y":
        cheese=input("if you want extra cheese y or n")
        if cheese=="y":
            print(f"you want to pay :${cost_of_medium_pizza+pepper_of_medium_pizza+extra_cheese}")
        else:
            print(f"your want to pay: ${cost_of_medium_pizza+pepper_of_medium_pizza}")
    else:
        cheese = input("if you want extra cheese y or n")
        if cheese=="y":
            print(f"you want to pay:${cost_of_medium_pizza+extra_cheese}")
        else:
            print(f"your bill is{cost_of_medium_pizza}")

elif pizza_size=="large":
    pepper=input("do you want papper y or n")
    if pepper=="y":
        cheese=input("if you want extra cheese y or n")
        if cheese=="y":
            print(f"you want to pay :${cost_of_large_pizza+pepper_of_large_pizza+extra_cheese}")
        else:
            print(f"your want to pay: ${cost_of_large_pizza+pepper_of_large_pizza}")
    else:
        cheese = input("if you want extra cheese y or n")
        if cheese == "y":
            print(f"you want to pay:${cost_of_large_pizza + extra_cheese}")
        else:
            print(f"your bill is{cost_of_large_pizza}")