def almost_there():
	num = int(input("Enter a Number: "))
	minus1  = 100 - num
	minus2 = num - 100
	minus3 = 200 - num
	minus4 = num - 200 /
	minus1 = abs(minus1)
	minus2 = abs(minus2)
	minus3 = abs(minus3)
	minus4 = abs(minus4)
	if minus1 <=10:
		return True
	elif minus2<=10:
		return True
	elif minus3<=10:
		return True
	elif minus4<=10:
		return True	
	else:
		return False
result = almost_there()
print(result)