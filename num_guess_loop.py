# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program displays a random correct guess

import random


def guess_the_number():
    """Generates a random number and prompts the user to guess it."""
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess_str = input("Take a guess: ")
            guess = int(guess_str)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
                )
                break  # Exit the loop when the guess is correct

        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    guess_the_number()
