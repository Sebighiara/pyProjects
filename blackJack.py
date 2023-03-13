import random

#Create a deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	#when asking to print a card, return a string in the form "two of hearts"
	def __str__(self):
		return f"{self.rank} of {self.suit}"


class Deck():

	#create the deck
	def __init__(self):
		self.deck = [] #start with an empty list

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def shuffle(self):
		random.shuffle(self.deck)

	#return the last card of the deck after shuffling it
	def deal(self):
		singleCard = self.deck.pop()
		return singleCard

class Hand():

	def __init__(self):
		self.cards = [] #starting with an empty list
		self.value = 0
		self.aces = 0 

	def addCard(self, value):
		#add card from Deck.deal() --> single Card(suit, rank) 
		self.cards.append(Card)
		self.value += values[Card.rank] #take from the dict only the numbers

		#track aces
		if Card.rank == 'Ace':
			self.aces += 1

	def showAll(self):
		singleCard = ''
		for singleCard in self.cards:
			print(singleCard)

	def showSome(self):
		singleCard = ''
		for singleCard in self.cards - 1:
			print(singleCard)
		print("one card hidden")


	def adjustAces(self):

		#while value is over 21 and i still have aces
		#adjust an ace to the value of 1 instead of 11
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -=1


class Chips():

	def __init__(self, total = 100):

		self.total = total
		self.bet = 0

	def winBet(self):

		self.total += self.bet

	def loseBet(self):
		self.total -= self.bet 


#function that will take the bet from player
def takeBet(chips):

	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Sorry, please provide an integer!")
		else:
			if chips.bet > chips.total:
				print(f"You don't have enough chips, you have {chips.total}")
			else:
				print("Thank you!")
				break

#function for taking hits
def hit(deck, hand):

	singleCard = deck.deal()
	hand.addCard(singleCard)
	hand.adjustAces()

def hitOrStand(deck, hand):
	global playing #used for an upcoming while loop in the code 

	while True:

		answer = input("Stand or hit? Enter s or h")
		if answer[0].lower() == 'h':
			hit(deck, hand)
		elif answer[0].lower() == 's':
			print("Player stands, dealer's turn!")
			playing = False
		else:
			print("I don't understand what you mean, please enter h or s!")
			continue
		break


def playerBusts(player, dealer, chips):
	print("Player BUST!")
	chips.loseBet()

def playerWins(player, dealer, chips):
	print("Player WIN!")
	chips.winBet()

def dealerBusts(player, dealer, chips):
	print("Player WIN!")
	chips.winBet()

def dealerWins(player, dealer, chips):
	print("Dealer WIN!")
	chips.loseBet()

def push(player, dealer):
	print("Dealer and player tie, PUSH!")


while True:

	print("Welcome to BLACK JACK game!")

	#create deck, shuffle and deal two cards to each other
	deckCards = Deck()
	deckCards.shuffle()
	
	playerHand = Hand()
	playerHand.addCard(deckCards.deal())
	playerHand.addCard(deckCards.deal())


	dealerHand = Hand()
	dealerHand.addCard(deckCards.deal())
	dealerHand.addCard(deckCards.deal())

	#set up the player's chips
	playersChips = Chips()

	#prompt the player for their bet
	takeBet(playersChips)

	#show cards (but keep one dealer's card face down)
	print("PLAYER HAND")
	playerHand.showAll()
	print("DEALER HAND")
	dealerHand.showSome()

	while playing:

		#prompt for player to hit or stand
		hitOrStand(deckCards, playerHand)

		#show cards but keep one dealer's card face down
		showSome(playerHand, dealerHand)

		#if player hand's exceeds 21, run playerBusts() and break out of loop
		if playerHand.value > 21:
			playerBusts(playerHand, dealerHand, playersChips)

			break

		#if player hasn't busted, play dealer's untill reaches 15
		while playerHand < 21:
			hit(deckCards, dealerHand)

		#show all cards
		print("PLAYER HAND")
		playerHand.showAll()
		print("DEALER HAND")
		dealerHand.showAll()

		#run different winning scenarios
		if dealerHand.value > 21:
			dealerBusts(playerHand, dealerHand, playersChips)
		elif dealerHand.value > playerHand.value:
			dealerWins(playerHand, dealerHand, playersChips)
		elif dealerHand.value < playerHand.value:
			playerWins(playerHand, dealerHand, playersChips)
		else:
			push(playerHand, dealerHand)

		#inform player about his chips
		printf(f"Ypu've got {playersChips.total} chips")

		#ask to play again
		playAgain = input("Do you want to play again? y or n")

		if playAgain[0].lower() == 'y':
			playing = True
			continue
		else:
			print("Thank you for playing!")
			break















