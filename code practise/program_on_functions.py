from operator import truediv
#truediv is used for true division
a=truediv(10,3)
print(round(a,2))


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

'''def canbuyalcohol(age):
    if age>=18:
        print("you can buy alcohol")
        return True

    else:
        print("your children ")
        return False

age=int(input("enter your age:"))
canbuyalcohol(age)'''
def canbuyalcohol(age):
    if type(age)!=int:
        print("enter your age in numbers")
        return


    elif age>=18:
        print("you can buy alcohol")
        return True
    else:
        print("you are children")
        return False
age=input("enter your age")
canbuyalcohol(age)