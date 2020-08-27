def money_permonth(fix,goodamount):
	good = int(input("Enter the Number of good things done this month: "))
	a  = fix + good * goodamount
	return a 
result = money_permonth(100,10)
print(result)