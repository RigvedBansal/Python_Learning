def count_prime(num):
	primes = [2]
	x = 3
	if num < 2:
		return 0
	while x <= num:
		for y in range(3,x,2):
			if x%y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2
	return primes

def largest_prime(list,num):
	mylist = []
	for item in list:
		if num % item == 0:
			mylist.append(item)
	return mylist[-1]		
result = count_prime(13195)
result2 = largest_prime(result,13195)
print(result2)