import random

class Player():
	def __init__(self, name, colour):
		self.name = name
		self.colour = colour

	def getDescription(self):
		return self.name + " with colour: " + self.colour

player1 = Player("Connor", "Red")
player2 = Player("John", "Blue")

currentPlayer = 1
hiddenNumber = random.randint(1,100)
print("OK I’m thinking of a number - please take turns to try to guess it")
print("Players in the game are:")
print("Player 1 is: " + player1.getDescription())
print("Player 2 is: " + player2.getDescription())
while True:
	print("Player " + str(currentPlayer) + " turn")
	if (currentPlayer == 1):
		currentPlayerName = player1.name 
		currentPlayerColour = player1.colour
	else:
		currentPlayerName = player2.name 
		currentPlayerColour = player2.colour
 
	print("Player " + currentPlayerColour + ", please take your turn " + currentPlayerName)
 
	# Allow player to choose their number
	playerChoice = int(input("Choose your number from 1-100: "))
	print("You chose: " + str(playerChoice))

	# check player’s choice against hiddenNumber
	if playerChoice == hiddenNumber:
		print("Correct! You won the game")
		break
	else:
		message = "higher than" if hiddenNumber > playerChoice else "lower than"
		print("That's not right. The number I'm thinking of is " + message + " your number")
	
	if currentPlayer == 1:
		currentPlayer = 2 
	else:
		currentPlayer = 1

# The winner will be currentPlayer
if (currentPlayer == 1):
	print("The winner is Player 1: " + player1.getDescription())
else:
	print("The winner is Player 2: " + player2.getDescription())
