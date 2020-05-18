import random

class Player():
	def __init__(self, name, colour):
		self.name = name
		self.colour = colour

player1 = Player("Connor", "Red")
player2 = Player("John", "Blue")

player1Name = "Connor"
player1Colour = "Red"
player2Name = "John"
player2Colour = "Blue"
currentPlayer = 1
hiddenNumber = random.randint(1,100)
print("OK I’m thinking of a number - please take turns to try to guess it")
print("Players in the game are:")
print("Player 1 is: " + player1Name + " with colour: " + player1Colour)
print("Player 2 is: " + player2Name + " with colour: " + player2Colour)
while True:
	print("Player " + str(currentPlayer) + " turn")
	if (currentPlayer == 1):
		currentPlayerName = player1Name 
		currentPlayerColour = player1Colour
	else:
		currentPlayerName = player2Name 
		currentPlayerColour = player2Colour
 
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
	print("The winner is Player 1: " + player1Name + " with colour " + player1Colour)
else:
	print("The winner is Player 2: " + player2Name + " with colour " + player2Colour)
