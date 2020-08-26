listof3digits = [x for x in range(100,1000)]
maxpalindrome = 0
for item1 in listof3digits:
	for item2 in listof3digits:
		mystr = str(item1 * item2)
		if mystr == mystr[::-1]:
			if int(mystr) > maxpalindrome:
				maxpalindrome  = int(mystr)
print(maxpalindrome)				