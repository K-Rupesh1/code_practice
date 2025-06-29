import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    should_accumulate=True
    num1 = float(input("enter a number:"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        choose=input(f"choose a symbol")
        num2=float(input("enter second number:"))
        answer=operations[choose](num1,num2)
        print(f"{num1}{choose} {num2}={answer}")

        choice=input("type 'y' to calculate another number with answer type 'n' to exit")
        if choice=="y":
            num1=answer
        else:
            should_accumulate=False

calculator()

