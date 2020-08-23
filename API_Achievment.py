#Methods
def ask_name():
	name = str(input("Enter Your name: "))
	print(f'Hello {name}')
	return name
def ask_age():
    age = int(input("Enter Your age: "))
    return age
def ask_country():
    country = str(input("Which country do you live in? "))
    return country
def return_info(name,age,country):
	print(f'Hello {name}, You are {age} years old, You live in {country}')
#defined Variables
name = ask_name()
age = ask_age()
country = ask_country()
#executed methods
return_info(name,age,country)
#Saving the Entries
api = open('api.txt','a+')
api.write(f'\nName = {name} Age = {age} Country = {country}')
api.close()
#Program Ending Alert
print("Program has Ended")