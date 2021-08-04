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
	
	return choice


#this is a function where the user can choose where to put X or 0
def positionChoice(board):

	global symbol

	position = int(input('Choose your next position: (1, 9)'))

	#replace the blank spaces with X or 0
	if symbol == 'X':
		board[position] = symbol
		symbol = '0'
	else:
		board[position] = symbol
		symbol = 'X'

	#display the board everytime a player makes a move
	displayBoard(board)


#this is a function that will return True if a player has won or Flase in the other case
def playerWin(board):

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


def gameOnChoice():

	choice = input('Do you want to keep playing (Y or N)? ')

	return choice == 'Y'

#Global variables
board = [' '] * 10
gameOn = True

while gameOn:

	symbol = playerChoice()
	
	while playerWin(board) == False or ' ' in board:
		positionChoice(board)

	if playerWin(board):
		print('Congratulations, you have won the game!')
	elif ' ' not in board:
		print('Tie')
	else:
		pass

	gameOn = gameOnChoice()


