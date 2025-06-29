def format_name(f_name,l_name):
 formatted_f_name=f_name.title()
 formatted_l_name=l_name.title()
 return f"{formatted_f_name}{formatted_l_name}"
print(format_name("rupesh","k"))# it calling a function with arguments

def function1(text):
    return text+text
def function2(text):
    return text
output=function1("hello")
print(output)
output1=function2("Rupesh")
print(output1)