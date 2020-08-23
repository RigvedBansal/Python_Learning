def old_macdonald():
	text = input("Enter a String: ")
	mystr = []
	for letter in text:
		mystr.append(letter)
	mystr[0]=mystr[0].upper()
	mystr[3]=mystr[3].upper()
	text = ''
	for item in mystr:
		text = text + item
	return text
result = old_macdonald()	
print(result)