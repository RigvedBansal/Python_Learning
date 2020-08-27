class Dog():

	species = 'mammal'

	def __init__(self,breed,name,spots):

		self.breed = breed
		self.name = name
		self.spots = spots

	def walk(self):
		print("TAKE THE DOG FOR A WALK!!!!")

	def bark(self,number):	
		print(f'WOOF! My name is {self.name} and the number is {number}')


myDog = Dog("German Shephard","Tommy",False)
print(myDog.breed)
print(myDog.name)
print(myDog.spots)
print(myDog.species)
myDog.bark(23)
myDog.walk()