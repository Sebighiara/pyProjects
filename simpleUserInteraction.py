
def displayGame(gameList):
	print("There is the game list: ")
	print(gameList)


def positionChoice():

	#VARIABLES
	choice = "wrong"

	withinNumbers = ['0', '1', '2']

	#user choice validation
	while choice.isdigit() == False or choice not in withinNumbers:

		choice = input("Pick a position number (0, 1, 2): ")

		if choice.isdigit():
			if choice not in withinNumbers:
				print("The number you chose is not in range 0, 2")

		else:
			print("Sorry, type a digital number")

	return int(choice)


def replacementUser(gameList, position):

	#replacing the element in the position given with a string
	userPlacement = input("Type a string you want to replace in that position: ")

	gameList[position] = userPlacement

	return gameList


def gameOnChoice():

	choice = 'wrong'

	#game over decision
	while choice not in ['Y', 'N']:

		choice = input("Keep playing (Y or N)? ")

		if choice not in ['Y', 'N']:
			print("Please choose between Y or N")

	return choice == "Y"

gameList = [0, 1, 2]

gameOn = True


while gameOn:
	displayGame(gameList)

	position = positionChoice()

	gameList = replacementUser(gameList, position)

	displayGame(gameList)

	gameOn = gameOnChoice()







