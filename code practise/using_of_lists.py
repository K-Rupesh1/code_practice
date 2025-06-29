fruits=["cherry","apple","pear"]
print(fruits)

fruits.append("banana")
print(fruits)

fruits.insert(2,"grapes")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.__delitem__(1)
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia",
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                     "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio",
                     "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama",
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
                     "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
states_of_america.pop(1)
print(states_of_america)

a=len(states_of_america)
print(a)

states_of_america.append("aaa") # it will add at the last index..it is not suitable for choosing a index
print(states_of_america)

states_of_america.insert(1,"ccc")
print(states_of_america)

