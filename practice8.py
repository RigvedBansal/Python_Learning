def paper_doll():
	mystr = input("Enter a String: ")
	text = ''
	for letter in mystr:
		text = text + letter * 3
	return text
result = paper_doll()
print(result)		