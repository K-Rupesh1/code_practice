colours={"apple":"red","pear":"green","banana":"yellow"}#it will allocate like key:value
print(colours["apple"])

#adding element into dictionary
colours["peach"]="pink"
print(colours)
#edit a element in dictonary
colours["apple"]="green"
print(colours)

for key in colours:
    print(key)
for values in colours:
    print(colours[values])