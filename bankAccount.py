
class Account():

	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

	def deposits(self, depValue):
		self.balance = self.balance + depValue
		print("Deposit accepted")

	def withdraw(self, withdValue):
		money = self.balance - withdValue
		if money >= 0:
			self.balance = self.balance - withdValue
			print("Withdraw accepted!")
		else:
			print("Funds Unavailable!")

		

owner = input("Enter the owner's name: ")
balance = int(input("Enter the owner's balance: "))
acct1 = Account(owner, balance)

print(acct1)

print(acct1.owner)
print(acct1.balance)
depValue = int(input("Enter the sum you want to deposit: "))
acct1.deposits(depValue)
print(f"Now your balance is: {acct1.balance}")

withdValue = int(input("Enter the sum you want to withdraw: "))
acct1.withdraw(withdValue)
print(f"Your balance is: {acct1.balance}")

withdValue = int(input("Enter the sum you want to withdraw: "))
acct1.withdraw(withdValue)
print(acct1.balance)