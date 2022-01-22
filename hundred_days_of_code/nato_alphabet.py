# Read the nato alphabets file
import pandas as pd

file_path = "../input/nato_phonetic_alphabet.csv"
nato_dict = {}


def using_dictionary():
    """
    Read the file using file and create the dict
    :return:
    """
    with open(file_path) as file:
        lines = file.read().splitlines()

    global nato_dict
    nato_dict = {line.split(",")[0]: line.split(",")[1] for line in lines[1:]}


def using_pandas():
    """
    Read the file using pandas and create the dict
    :return:
    """
    global nato_dict
    data = pd.read_csv(file_path)
    nato_dict = {row.letter: row.code for index, row in data.iterrows()}


def get_nato_words():
    # Create a list of the phonetic code words from a word that the user inputs.
    inp = input("Enter a word to generate nato phonetic words::")
    nato_words = {let.upper(): nato_dict.get(let.upper(), "NotFound") for let in inp}
    print(nato_words)


# using_dictionary()
using_pandas()
get_nato_words()
