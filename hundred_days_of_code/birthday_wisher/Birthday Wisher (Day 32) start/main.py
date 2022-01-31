from datetime import datetime as dt
import random

def get_quotes():
    with open("quotes.txt") as inp:
        return inp.read().splitlines()


def send_email():
    if dt.now().weekday() == 0:
        print(random.choice(get_quotes()))


send_email()
