class Animal():

	def __init__(self):
		print("ANIMAL CREATED")

	def who_am_i(self):
		print("I AM AN ANIMAL")

	def eat(self):
		print("I AM EATING")

class Dog(Animal):

	def __init__(self):
		Animal.__init__(self)
		print("Dog CREATED")

	def who_am_i(self):
		print("I AM A DOG")

	def eat(self):
		print("I AM EATING DOG FOOD")

	def bark(self):
		print("WOOF!!!")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()
my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()