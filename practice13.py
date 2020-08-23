def return_s():
	text = input("Enter A String: ")
	for word in text.split():
		if word[0]=='s':
			print(word)
return_s()		