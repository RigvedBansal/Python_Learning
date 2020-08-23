def square(num):
	return num**2

def splicer(mystring):
	if len(mystring)%2 ==0:
		return "EVEN"
	else:
		return mystring[0]
def check_even(num):
	return num%2==0
mynums = [1,2,3,4,5]
for item in map(square,mynums):
	print(item)	
list1 = list(map(square,mynums))
print(list1)
names = ['Andy','Eve','Sally']
list2 = list(map(splicer,names))
print(list2)
mynums = [1,2,3,4,5,6]
list3 =list(filter(check_even,mynums))
print(list3)