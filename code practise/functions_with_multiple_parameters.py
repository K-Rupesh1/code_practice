# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

#function with multiple inputs
def greet_with(name,greeting):
    print(f"{name},{greeting}")

greet_with("rupesh","how are you")

#passing parameters name and location into function
def name_location(name,location):
    print(f"{name} your in {location}")
name_location("rupesh","narasapuram")

#potential arguments
def my_function(a,b):
    print(a)
    print(b)
my_function(2,1)

#calling a functiion by using a keywords
name_location(name="rupesh",location="k.narasapuram")



