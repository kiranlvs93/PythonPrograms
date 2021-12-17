"""
This program is to find the highest bidder from an auction
Takes 2 inputs - name and bid value
The program takes as many bids as the user wants and once there are no bidders, it announces the winner
"""

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bidders = {}


def clear():
    """
    Clear the console
    If you are using PyCharm, make sure the Run Configuration setting, "Emulate terminal in output console" is checked
    :return:
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_winner(bids):
    """
    Find the winner from the given bids
    :param bids:
    :return:
    """
    highest_bid = 0
    # One liner for finding the winner.
    # Find the maximum bid -> get the position of that bid in values list
    # Then get the key corresponding at that position from the list of keys
    winner = list(bids.keys())[list(bids.values()).index(max(bids.values()))]
    # You can use the below also.
    # for bidder, value in bids.items():
    #     if value > highest_bid:
    #         winner = bidder
    #         highest_bid = value
    print(f"The winner is {winner.upper()} with a bid of ${bids[winner]}")



while True:
    name = input("What is your name?:")
    bid_value = int(input("What is your bid?:$"))
    bidders[name] = bid_value
    inp = input("Are there any other bidders? Type 'yes' or 'no'::")
    if inp == 'no':
        clear()
        print(logo)
        get_winner(bidders)
        break
    elif inp == 'yes':
        clear()
        print(logo)
