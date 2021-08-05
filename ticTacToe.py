#this is a function that will display the game board
def displayBoard(board):

	#this is the board printed
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('---------')
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('---------')
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])



#this is a function where the user can decide whether is X or 0
def playerChoice():
	
	choice = input('Player 1: Do you want to be X or 0?')
	
	if choice == 'X':
		print('Player 1 will start')
	elif choice == '0':
		print('Player 2 will start')
	else:
		print("Sorry, we don't understand, type again... ")
		playerChoice()


#this is a function where the user can choose where to put X or 0
def positionChoice(board):

	global symbol

	position = int(input('Choose your next position: (1, 9)'))

	#the symbol will change after a user makes a move
	if symbol == 'X':
		symbol = '0'
	else:
		symbol = 'X'

	#replace the blank spaces with X or 0
	board[position] = symbol

	#display the board everytime a player makes a move
	displayBoard(board)


#this is a function that will return True if a player has won or Flase in the other case
def playerWin(board, symbol):

	#Check if there are verticals, horizontals or diagonals for a win
	if (symbol == board[1] == board[2] == board[3]) or \
		(symbol == board[4] == board[5] == board[6]) or \
		(symbol == board[7] == board[8] == board[9]) or \
		(symbol == board[1] == board[4] == board[7]) or \
		(symbol == board[2] == board[5] == board[8]) or \
		(symbol == board[3] == board[6] == board[9]) or \
		(symbol == board[1] == board[5] == board[9]) or \
		(symbol == board[3] == board[5] == board[7]):
		return True
	else:
		return False

#This is a function that returns True if the user wants to play again or Flase otherwise
def gameOnChoice():

	choice = input('Do you want to keep playing (Y or N)? ')

	return choice == 'Y'


gameOn = True

while gameOn:

	#the board will be cleared everytime the user wants to play again
	board = [' '] * 10
	board[0] = '#'

	#user choose if he wants to play with "x" or "0"
	playerChoice()

	symbol = '0'
	space = ' '
	
	#keep moving positions until one of them wins or there is a tie
	while playerWin(board, symbol) == False and space in board:

		positionChoice(board)

	if playerWin(board, symbol):
		print('Congratulations, you have won the game!')
	elif space not in board:
		print('Tie')
	else:
		pass

	#asking for playing again
	gameOn = gameOnChoice()
