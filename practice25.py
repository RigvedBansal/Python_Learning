try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print("oops error occured")

try:
	x = 5
	y = 0
	z = x/y	
	print(z)
except ZeroDivisionError:
	print("oops ZeroDivisionError occured")

def ask():
	while True:
		try:
			int1 = int(input("Enter a Number: "))
		except ValueError:
			print("oops not an int")
			continue
		else:
			print(int1 ** 2)
			break
ask()			