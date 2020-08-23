def animal_crackers():
	text = input("Enter a Two word string: ")
	text_List = text.split()
	if text_List[0][0]==text_List[1][0]:
		return True
	else:
		return False	
result = animal_crackers()
print(result)