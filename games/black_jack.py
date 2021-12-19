############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
###############################################################

import random
import utilities.ascii_art as art
from utilities.cmd_operations import clear

dealer_cards = []
player_cards = []
player_score = 0
dealer_score = 0


def draw_card(score):
    """
    Function to hand a card to either of the users.
    If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead
    :param score:
    :return:
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    card = 1 if card == 11 and score + card > 21 else card
    return card


def get_score(dont_display=True):
    """
    Function to get the score.
    :param dont_display: If this is set to False, scores are printed onto console
    :return: Scores of player and dealer
    """
    global player_score, dealer_score
    player_score, dealer_score = sum(player_cards), sum(dealer_cards)
    if not dont_display:
        print(f"\tYour cards:{player_cards}, Current score: {player_score}")
        print(f"\tDealer cards:{dealer_cards[0]}")
    return player_score, dealer_score


def check_blackjack():
    """
    Checking if either the player or the dealer have got blackjack.
    If both of them have blackjack then its the dealer that wins else the one who gets BJ wins
    :return:
    """
    global player_score, dealer_score
    player_score, dealer_score = get_score()
    if dealer_score == 21 and player_score == 21:
        winner = "Computer"
        end_game(winner, "blackjack")
        return True
    elif dealer_score == 21 or player_score == 21:
        winner = "You" if player_score == 21 else "Computer"
        end_game(winner, "blackjack")
        return True
    else:
        return False


def start_game():
    """
    Start the game
    :return:
    """
    global player_score, dealer_score
    print(art.black_jack)
    # Give both the player and the dealer a pair of cards
    for _ in range(2):
        dealer_cards.append(draw_card(dealer_score))
        player_cards.append(draw_card(player_score))
    player_score, dealer_score = get_score(False)
    return check_blackjack()


def end_game(winner, condition):
    """
    Print appropriate message at the end of the game
    :param winner:
    :param condition:
    :return:
    """
    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
    if condition == 'over':
        print("You went over. You lose :-(" if winner == "Computer" else "Opponent went over. You win :-)")
    elif condition == 'win':
        print("You win :-)" if winner == "You" else "You lose :-(")
    elif condition == "blackjack":
        print("ITS A BLACK JACK. You win :-)" if winner == "You" else "You lose. Opponent has BLACK JACK :-(")
    elif condition == "draw":
        print("Its a DRAW")
    print("***************************************")


def check_status():
    """
    Check status of the game after drawing card everytime
    :return:
    """
    global player_score, dealer_score
    player_score, dealer_score = get_score()
    # Check if either of the players have got blackjack
    if check_blackjack():
        return True
    # Check if either of the players have got over 21
    elif dealer_score > 21 or player_score > 21:
        winner = "You" if dealer_score > 21 else "Computer"
        end_game(winner, "over")
        return True
    # If both dealer score and player score > 16 and if both scores are same then its DRAW
    elif dealer_score > 16 and player_score > 16 and dealer_score == player_score:
        end_game(None, "draw")
        return True
    # If either dealer score or player score > 16
    elif dealer_score > 16 or player_score > 16:
        winner = "You" if dealer_score < player_score else "Computer"
        end_game(winner, "win")
        return True
    # Display the score and continue the game
    else:
        get_score(False)
        return False


def play_game():
    """
    Begin the game
    :return:
    """
    global player_cards, dealer_cards
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
        clear()
        player_cards, dealer_cards = [], []
        game_over = start_game()
        while not game_over:
            if input("Type 'y' to get another card, type 'n' to pass::") == 'y':
                player_cards.append(draw_card(player_score))
                game_over = check_status()
            else:
                if dealer_score > 16:
                    game_over = check_status()
                else:
                    while dealer_score <= 16:
                        dealer_cards.append(draw_card(dealer_score))
                        game_over = check_status()
        play_game()
    else:
        print("GAME ENDED. Have a good day!!")


play_game()
