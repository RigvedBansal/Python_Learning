def makes_twenty():
	num = int(input("Enter a Number: "))
	num1 = int(input("Enter a Second Number: "))
	if num + num1 == 20:
		return True
	else:
		return False

result = makes_twenty()
print(result)	