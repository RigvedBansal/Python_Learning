import random
def gen_random(n,l,h):
	for i in range(n):
		yield random.randint(l,h)
rand_list = list(gen_random(10,100,1000))
print(rand_list)
random_int = gen_random(10,100,1000)
print(next(random_int))
print(next(random_int))
print(next(random_int))
print(next(random_int))
print(next(random_int))