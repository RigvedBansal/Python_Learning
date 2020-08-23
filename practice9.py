def blackjack():
	num=int(input("Enter Number between 1 and 11: "))
	num1=int(input("Enter Number between 1 and 11: "))
	num2 = int(input("Enter Number between 1 and 11: "))
	if num + num1 + num2 <= 21:
		return num+num1+num2
	else:
		if num == 11 or num2 == 11 or num1 == 11:
			sum1 = num1+num+num2 - 10 
			if sum1 <= 21:
				return sum1	
		else:
			return 'BUST'
result = blackjack()
print(result)