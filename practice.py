def myfunc():
	str = input("Enter a Word: ")
	mystr=''
	index = 0
	while index < len(str):
		if index % 2 == 0:
			mystr = mystr+str[index].upper()
		else:
			mystr= mystr+str[index].lower()
		index+=1
	return mystr

result = myfunc()
print(result)            