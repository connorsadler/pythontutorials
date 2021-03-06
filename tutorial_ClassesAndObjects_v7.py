import random

class Player():
	def __init__(self, number, name, colour):
		self.number = number
		self.name = name
		self.colour = colour

	def getDescription(self):
		return self.name + " with colour: " + self.colour

playerList = []
playerList.append(Player(1, "Connor", "Red"))
playerList.append(Player(2, "John", "Blue"))

currentPlayer = playerList[0]
hiddenNumber = random.randint(1,100)
print("OK I’m thinking of a number - please take turns to try to guess it")
print("Players in the game are:")
print("Player 1 is: " + playerList[0].getDescription())
print("Player 2 is: " + playerList[1].getDescription())
while True:
	print("Player " + str(currentPlayer.number) + " turn")
	print("Player " + currentPlayer.colour + ", please take your turn " + currentPlayer.name)
 
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
	
	if currentPlayer == playerList[0]:
		currentPlayer = playerList[1]
	else:
		currentPlayer = playerList[0]

# The winner will be currentPlayer
print("The winner is: " + currentPlayer.getDescription())
