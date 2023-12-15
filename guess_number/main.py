import random
from art import logo

print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)
if level == 'easy':
    attempts = 10
else:
    attempts = 5


def trytoguess(attempts):
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if number == guess:
            print(f"You got it! The answer is {number}.")
            return
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")
        attempts -= 1

    print("You've run out of guesses, you lose.")


trytoguess(attempts)
