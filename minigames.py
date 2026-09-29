import random

words = ["red", "green", "yellow", "orange", "pink", "blue"]

word = random.choice(words)
guessedLetters = []
maxAttempts = 6
wrongGuesses = 0

print("Welcome to the Hangman Game!")

while wrongGuesses < maxAttempts:
    display = ""

    for letter in word:
        if letter in guessedLetters:
            display += letter + " "
        else:
            display += "_ "

    print("Wrong guess:", wrongGuesses)
    print("Guessed letters:", guessedLetters)
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        print("The word is:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessedLetters:
        print("You already guessed that letter.")
        continue

    guessedLetters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrongGuesses += 1
        print("Wrong guess!")

else:
    print([wrongGuesses])
    print("Game Over!")
    print("The correct word was:", word)