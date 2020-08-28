class Account():

	def __init__(self,owner,amount):
		self.owner = owner
		self.amount = amount

	def deposit(self,deposit):
		self.amount += deposit
		print("Bank balance = "+str(self.amount))

	def withdraw(self,withdrawal):
		if withdrawal > self.amount:
			print("Amount unavailable")
			print("Bank balance = "+str(self.amount))
		else:
			self.amount -= withdrawal
			print("Bank balance = "+str(self.amount))

name = input("Enter the Name of the owner of the Account:")
amount = int(input("Enter the Amount in the Bank Account: "))
Account1 = Account(name,100000)

quit = False
print("Press 1 for the list of actions\nPress 2 for making a Deposit\nPress 3 for making a Withdrawal\nPress 4 for knowing the Bank Balance\nPress 5 for quitting")
while not quit:
	num = int(input("Enter An Action Number: "))
	if num == 1:
		print("Press 1 for the list of actions\nPress 2 for making a Deposit\nPress 3 for making a Withdrawal\nPress 4 for knowing the Bank Balance\nPress 5 for quitting")
	elif num==2:
		Amount = int(input("Enter the Amount You want to deposit: "))
		Account1.deposit(Amount)
	elif num == 3:
		Amount = int(input("Enter the Amount you want to withdraw: "))
		Account1.withdraw(Amount)
	elif num == 4:
		print(Account1.amount)
	elif num == 5:
		print("QUITTING")
		quit = True
	else:
		pass