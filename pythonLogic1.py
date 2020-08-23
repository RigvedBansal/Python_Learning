def is_List_Even(mylist):
	even_numbers = []
	for num in mylist:
		if num % 2 == 0:
			even_numbers.append(num)
		else:
		    pass
	return even_numbers

mylist = [1,2,3,4,5,6,7,8,9,10]	
even_numbers = is_List_Even(mylist)
print(even_numbers)