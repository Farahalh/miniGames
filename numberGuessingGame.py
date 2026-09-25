# Number Guessing Game
# Save a numeric value to a variable as the correct answer
# The player will, through the console, try to guess the correct value
# For every guess the player will be notified if the guess value is to low, to high or correct
# If the guess is wrong the game will continue
# If the guess is correct the game will end and the player will be notified of how mny tries the had before gettign it right 

correctAnswer = 24

while True:
    try:
        userInput = int(input("Please enter a numeric value that you think is the correct answer: "))
        number = int(userInput)
        if number < correctAnswer:
            print("Number guessed is too low, try again!")
        elif number > correctAnswer:
           print("Number guessed is too high, try again!")
        else:
            print("Congratulations, you guessed the correct number!")
            break
    except ValueError:
        print("Invalid input, please enter a valid number.")