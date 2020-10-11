def sum_of_primes(num):
	sum = 2
	x = 3
	if num < 2:
		return 0
	while x <= num:
		for y in range(3,x,2):
			if x%y == 0:
				x += 2
				break
		else:
			sum+=x
			x += 2
	return sum

print(sum_of_primes(2000000))