def sum_of_3_5(num):
	total = 0
	a = 1
	while a <= num:
		if a % 5 == 0 or a % 3 == 0:
			total += a
			a+=1
		else:
			a+=1
	return total
result = sum_of_3_5(1000)
print(result)			