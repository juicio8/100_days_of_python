import random

from hangman_art import logo, stages
from hangman_words import word_list
word_to_guess = random.choice(word_list)
print(word_to_guess)
guessed = []
length = len(word_to_guess)
lives = 6

print(logo)
for n in range(len(word_to_guess)):
    guessed.append('_')

while length and lives:
    guess = input('Make a guess: ').lower()
    right = False
    if guess in guessed:
        print("You've already guessed this letter\n")
    else:
        for n in range(len(word_to_guess)):
            if guess == word_to_guess[n]:
                guessed[n] = word_to_guess[n]
                length -= 1
                right = True
        if not right:
            lives -= 1
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
            print(f"{stages[lives]}\n")
        else:
            print(' '.join(guessed))
            print()
if not lives:
    print("You lose.")
else:
    print("You win")
