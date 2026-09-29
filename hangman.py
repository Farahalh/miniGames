# Hangman
# Save a text value as correctAnswer in a variable
# The player, through the console, try to guess the correct word
# For every guess the player gets to see the guess, whether it is correct or not
# For every guess the player will see all wrong and right guesses that was previously done
# For every guess the player will know how close they are to losing
# For every wrong guess, the player will get closer to losing
# If all the unique string characters guessed are correct, the player will know they have won and the game will end
# If the number of attempts are reached the player will know they have lost and the game will end.

correctAnswer = "farah"
guessedLetters = []
maxAttempts = 6
wrongGuesses = 0

while wrongGuesses < maxAttempts:
    display = ""

    for letter in correctAnswer:
        if letter in guessedLetters:
            display += letter + " "
        else:
            display += "_ "

    print([wrongGuesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        print("The word was:", correctAnswer)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessedLetters:
        print("You already guessed that letter.")
        continue

    guessedLetters.append(guess)

    if guess in correctAnswer:
        print("Correct guess!")
    else:
        wrongGuesses += 1
        print("Wrong guess!")

else:
    print([wrongGuesses])
    print("Game Over!")
    print("The correct word was:", correctAnswer)