import random

words = {
    "easy": ["red", "blue", "pink"],
    "hard": ["green", "yellow", "orange", "purple"]
}

print("Welcome to the Hangman Game!")
print("Choose a level:")
print("1. Easy")
print("2. Hard")

level = input("Choose a level: ")

if level == "1":
    word = random.choice(words["easy"])
    maxAttempts = 8

elif level == "2":
    word = random.choice(words["hard"])
    maxAttempts = 5

else:
    print("Invalid choice.")

guessedLetters = []
maxAttempts = 6
wrongGuesses = 0

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