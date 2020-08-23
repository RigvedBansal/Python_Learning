x = 25

def printer():
	x = 50
	return x
print(x)
print(printer())
print(x)
"""
Local - Namea assigned in any way within a function, and not declared global in that function
Enclosing function locals- Names in the local scope of any and all enclosing functions, from inner to outer.
Global (module)- Names assigned at the top - level of a module file, or declared global in a def within the file.
Built-in(Python) - Names pre - assigned in the built-in names ,module:
open,range,SyntaxError,,...
"""
#lambda num: num**2
#GLOBAL

name = 'THIS IS A GLOBAL STRING'

def greet():

#ENCLOSING

	name = "Sammy"

	def hello():

		name = 'IM A LOCAL'

		print('Hello '+name)

	hello()

greet()

x  = 50
def func():
	global x
	print(f'X is {x}')
	#LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
	x = 200
	print(f'I JUST LOCALLY CHANGED X TO {x}')
	func(x)