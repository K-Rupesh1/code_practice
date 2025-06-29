print("enter a name you want to print")
name=input()
count=(len(name))
print(count)
#print(name)
for i in range(count,0,-1):
     print(name[0:i])
print()

for i in range(0,count,1):
     print(name[0:i+1])

    

