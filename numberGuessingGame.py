# Number Guessing Game
# Save a numeric value to a variable as the correct answer
# The player will, through the console, try to guess the correct value
# For every guess the player will be notified if the guess value is to low, to high or correct
# If the guess is wrong the game will continue
# If the guess is correct the game will end and the player will be notified of how many tries they had before getting it right 

import random

numbers = [2, 1, 7, 5, 8, 3, 6, 4, 9]

number = random.choice(numbers)

maxAttempts = 10
attempts = 0

print("Welcome to Guess the Number!")

while attempts < maxAttempts:
    try:
        userInput = int(input("Please enter a numeric value betweeon 0 - 10: "))
        attempts += 1

        if userInput < number:
            print("Number guessed is too low, try again!")

        elif userInput > number:
           print("Number guessed is too high, try again!")

        else:
            print(f"Congratulations, you guessed the correct number! It only took you {attempts} tries!")
            break

    except ValueError:
        print("Invalid input, please enter a valid number.")

else:
    print("Game Over!")
    print(f"The correct number was {number}.")