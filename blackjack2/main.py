from art import logo
from utils import user_draw, dealer_draw, game, who_won, crossed_line


def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        print(logo)
        user = 0
        computer = 0
        drawn_cards = []
        dealer_cards = []
        while play == 'y':
            if (len(drawn_cards) == 0):
                user_draw(drawn_cards)
                dealer_draw(dealer_cards)
            user_draw(drawn_cards)
            if user > 21:
                break
            if computer <= 18:
                dealer_draw(dealer_cards)
            if computer > 21:
                break
            game(drawn_cards, dealer_cards[0])
            user = sum(drawn_cards)
            computer = sum(dealer_cards)
            play = input("Type 'y' to get another card, type 'n' to pass: ")
        if play == 'n' and computer <= 18:
            dealer_draw(dealer_cards)
        print(
            f"Your final hand: {drawn_cards}, final score: {sum(drawn_cards)}")
        print(
            f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

        if user > 21 or computer > 21:
            crossed_line(user, computer)
        else:
            who_won(user, computer)
        blackjack()
    else:
        return


blackjack()
