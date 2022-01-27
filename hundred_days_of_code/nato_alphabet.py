# Read the nato alphabets file
import pandas as pd
import re

file_path = "../input/nato_phonetic_alphabet.csv"
nato_dict = {}


def get_data_using_dictionary():
    """
    Read the file using file and create the dict
    :return:
    """
    with open(file_path) as file:
        lines = file.read().splitlines()

    global nato_dict
    nato_dict = {line.split(",")[0]: line.split(",")[1] for line in lines[1:]}


def get_data_using_pandas():
    """
    Read the file using pandas and create the dict
    :return:
    """
    global nato_dict
    data = pd.read_csv(file_path)
    nato_dict = {row.letter: row.code for index, row in data.iterrows()}


def get_nato_words():
    """
    Create a list of the phonetic code words from a word that the user inputs.
    Using regular expressions to find if there is a digit
    :return:
    """
    inp = input("Enter a word to generate nato phonetic words::")
    contains_digits = len(re.compile("\d+").findall(inp)) > 0
    while contains_digits:
        inp = input("Only letter are allowed in the alphabet. Numbers aren't allowed.\nEnter another word::")
        contains_digits = len(re.compile("\d+").findall(inp)) > 0
    nato_words = {let.upper(): nato_dict.get(let.upper(), "NotFound") for let in inp}
    print(nato_words)


def get_nato_words_exception_handling():
    """
    Using recursion and try_catch mechanism
    :return:
    """
    inp = input("Enter a word to generate nato phonetic words::")
    try:
        nato_words = {let.upper(): nato_dict[let.upper()] for let in inp}
    except KeyError:
        print("Numbers aren't allowed")
        get_nato_words_exception_handling()
    else:
        print(nato_words)


# using_dictionary()
get_data_using_pandas()
# get_nato_words()
get_nato_words_exception_handling()