def is_even(num):
	if num % 2 ==0:
		return True
	else:
		return False
mylist = [1,2]
a = 0
while a <=400000:
	mylist.append(mylist[a]+mylist[a+1])
	a+=1
#print(mylist)	
mylist = list(filter(is_even,mylist))
print(mylist)