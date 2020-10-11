def gensquares(n):
	for i in range(n):
		yield i**2

sq_list = list(gensquares(100))
print(sq_list)	
