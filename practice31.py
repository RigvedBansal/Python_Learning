def count_prime(num):
	primes = 2
	x = 3
	if num < 2:
		return 0
	while x < num:
		for y in range(3,x,2):
			if x%y == 0:
				x += 2
				break
		else:
			primes+=x
			x += 2
	return primes

primes = count_prime(2000000)
print(primes)