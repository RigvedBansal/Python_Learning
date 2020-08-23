def lesser_of_two_evens():
	a = int(input("Enter a Number "))
	b = int(input("Enter another Number "))
	if a % 2 == 0 and b % 2 == 0:
		if a > b:
			return b
		elif b > a:
			return a
		else:
			return a
	else:
		if a > b:
			return a
		elif b > a:
			return b
		else:
			return b
 
result=lesser_of_two_evens()
print(result)