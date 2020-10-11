import random
print(random.randint(0,100))
random.seed(101)
print(random.randint(0,100))
random.seed()
print(random.randint(0,100))
mylist = list(range(0,21))
print(random.choice(mylist))
#sample with replacement
print(random.choices(population=mylist,k=10))
#sample without replacement
print(random.sample(population=mylist,k=10))
random.shuffle(mylist)
print(random.uniform(0,10))