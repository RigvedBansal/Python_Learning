def master_yoda():
	text = input("Enter a string")
	mystr = text.split()
	text = ''
	a = 0
	for item in mystr:
		text = mystr[a] +' ' +text
		a+=1
	return text
result = master_yoda()
print(result)