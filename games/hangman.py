"""
Lets play HANGMAN game
This program generates a list of words and dumps the words into a file which is used for playing game
A random word from the above generated list is chosen and player has to guess word
I've web-scraping a website that generates the random words
"""
from requests_html import HTMLSession
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


def generate_words():
    """
    Scraping randomlists.com to generate words. The words are random and aren't repeated.
    :return:
    """
    no_of_words = input(
        "Enter the number of words you want to generate for using them in the game, subject to maximum of 2000::")
    url = f"https://www.randomlists.com/random-words?dup=false&qty={no_of_words}"
    print("Generating words.....")
    session = HTMLSession()
    r = session.get(url)
    r.html.render()
    print("Yaayyy!! Your words are generated. You are all set to play the game.")
    words_elements = r.html.find("li>.rand_large")
    word_list = [word.text for word in words_elements]
    return word_list


def get_display_word(display_word, word, guess):
    """
    Function to get the display word so that user knows where the letters guessed are located
    :param display_word:
    :param word:
    :param guess:
    :return:
    """
    positions = [pos for pos, ch in enumerate(word) if guess == ch]
    for pos in positions:
        display_word[pos] = guess
    return "".join(display_word)


def play_game(word_list=["hangman"]):
    """
    Game rules are implemented in this function
    :param word_list: list of words to chose from
    :return:
    """
    print("You have got 7 chances to save your man from going to the gallows. You either save him or we'll HANG him")
    word_to_guess = random.choice(word_list).upper()
    word_to_guess_copy = word_to_guess
    # print(f"Word list::{word_list}. Picked word::{word_to_guess}")
    misses = []
    display_word = list("_") * len(word_to_guess)
    print(f"Your word {''.join(display_word)}")
    while len(misses) < 7 and len(word_to_guess) > 0:
        print("-------------------------------------")
        guess = input("Guess a letter::").upper()
        if guess in word_to_guess:
            word_to_guess = word_to_guess.replace(guess, '')
            print(f"You guessed it right. You have got {len(word_to_guess)} more letters to guess")
            print(get_display_word(display_word, word_to_guess_copy, guess))
        else:
            misses.append(guess)
            print(stages[7 - len(misses)])
            print(f"You missed it. You have got {7 - len(misses)} chances remaining.")
            print(f"Wrong guesses:: {misses}")
            print(get_display_word(display_word, word_to_guess_copy, guess))
    if len(word_to_guess) == 0:
        print(f"Congratulations. You saved your man!!!")
    else:
        print(f"Alas. Your man is HANGED. The word was '{word_to_guess_copy}'.Better play next time :-(")


if __name__ == '__main__':
    no_of_rounds = input("Welcome to the world of hangman!!!\nHow many rounds would you like to play??")
    scraped_words = generate_words()
    print("We chose a random word for you to guess. Play carefully. The man is at your mercy now!!")
    for i in range(int(no_of_rounds)):
        print(f"**********************ROUND {i + 1}**********************")
        play_game(scraped_words)
    print(stages[0])
