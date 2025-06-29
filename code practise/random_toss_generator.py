import random
rand_numbers=random.randrange(1,10) #selecting the range from start to end
print(rand_numbers)

rand=random.random()*5  #the random will generate a range from 0.0 to 1.0
print(rand)

random_float=random.uniform(1,10)
print(random_float)
flip_coin=random.randint(0,1)
if flip_coin==0:
    print("the toss is head")
else:
    print("the toss is tail")
