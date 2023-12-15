import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck_size = len(deck) - 1


def user_draw(drawn_cards):
    drawn_cards.append(deck[random.randint(0, deck_size)])


def dealer_draw(dealer_cards):
    dealer_cards.append(deck[random.randint(0, deck_size)])


def game(drawn_cards, dealer_card):
    print(f"Your cards: {drawn_cards}, current score: {sum(drawn_cards)}")
    print(f"Computer's first hand {dealer_card}")


def crossed_line(user, computer):
    print(user, computer)
    if user > 21:
        print(f"You went over. Opponent wins!")
    elif computer > 21:
        print(f"Opponent went over. You win!")


def who_won(user, computer):
    print(user, computer)
    if user > computer:
        print("You win!!")
    elif computer > user:
        print("You loose")
    else:
        print("It's a tie!")
