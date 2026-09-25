# Number Guessing Game
# Save a numeric value to a variable as the correct answer
# The player will, through the console, try to guess the correct value
# For every guess the player will be notified if the guess value is to low, to high or correct
# If the guess is wrong the game will continue
# If the guess is correct the game will end and the player will be notified of how mny tries the had before gettign it right 

correctAnswer = 24;

playerGuess = input("Please enter a numeric value that you think is the correct answer: ");

numericValue = int(playerGuess)

print(type(numericValue))