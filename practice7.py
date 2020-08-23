def has_33(mylist):
	text = ''
	for item in mylist:
		text = text + str(item)
	a = 0
	for letter in text:
		if text[a] == '3' and text[a+1] == '3':
			return True
		else:
			pass	
		a+=1
	return False	
mylist = [3,3,4]
result = has_33(mylist)	
print(result)	