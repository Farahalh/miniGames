# Mini-Games

A Python console application with two mini-games: **Number Guessing Game** and **Hangman**.

## Number Guessing Game

The player tries to guess a hidden number through the console.

* Store a numerical value as the correct answer.
* The player enters guesses through the console.
* After each guess, tell the player if it is **too low**, **too high**, or **correct**.
* Continue until the correct answer is guessed.
* When the player wins, show how many guesses it took.

## Hangman

The player tries to guess the characters in a hidden word.

* Store a text value as the correct answer.
* The player guesses characters through the console.
* Tell the player whether each character is included in the correct answer.
* Show previous correct and incorrect guesses.
* Show how close the player is to losing.
* Each incorrect guess brings the player closer to losing.
* The player wins when all unique characters in the correct answer have been guessed.
* The player loses when the losing level is reached.

## Levels

Both games use sequences containing multiple correct answers.

* The player chooses a level before starting a game.
* The selected index determines which correct answer is used.
* Correct answers are hardcoded.

## Game Hub

A main menu lets the player choose which game to play:

1. Hangman
2. Number Guessing Game
3. Exit

## Git

The project is managed with Git and includes at least four commits. Changes to the correct answers can be made through a separate Git branch.
