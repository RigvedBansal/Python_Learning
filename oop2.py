class Circle():
	
	pi = 3.14

	def __init__(self,radius=1):
		self.radius = radius
		self.diameter = radius * 2 
		self.circumference = radius * self.pi * 2 
		self.area = self.pi * radius ** 2

myCircle = Circle(3)
print(myCircle.radius)
print(myCircle.diameter)
print(myCircle.circumference)
print(myCircle.area)
print(myCircle.pi)