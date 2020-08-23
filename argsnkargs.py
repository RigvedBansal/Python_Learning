def myfunc(**kwargs):
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')	
def myfunct(*args):
	return sum(args)

myfunc(fruit='apple')
result =myfunct(1,2,3,4,5,6,7,8,9,10)
print(result)