text = input("Enter a String: ")
mylist = text.split()
mylist1 = []
for item in mylist:
	if len(item) % 2 == 0:
		mylist1.append("EVEN")
	else:
		mylist1.append(item)
for item in mylist1:
	print(item)
