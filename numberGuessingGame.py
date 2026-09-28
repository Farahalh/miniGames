# Number Guessing Game
# Save a numeric value to a variable as the correct answer
# The player will, through the console, try to guess the correct value
# For every guess the player will be notified if the guess value is to low, to high or correct
# If the guess is wrong the game will continue
# If the guess is correct the game will end and the player will be notified of how many tries they had before getting it right 

attempts = 10
correctAnswer = 24
tries = 0

while tries < attempts:
    try:
        userInput = int(input("Please enter a numeric value that you think is the correct answer: "))
        number = int(userInput)
        if number < correctAnswer:
            print("Number guessed is too low, try again!")
        elif number > correctAnswer:
           print("Number guessed is too high, try again!")
        else:
            print(f"Congratulations, you guessed the correct number! It only took you {tries} tries!")
            break
        tries += 1
    except ValueError:
        print("Invalid input, please enter a valid number.")