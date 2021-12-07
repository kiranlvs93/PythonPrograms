from collections import Counter
import os
import re


def count_words(string, topn=20):
    """
    Count only words without number from a file
    :param topn: Most frequent words
    :param string: input string
    :return:
    """
    print("COUNTING WORDS WITHOUT NUMBERS.......")
    compiled = re.compile("\w+")
    words_list = [word.lower() for word in compiled.findall(string)]
    word_count = Counter(words_list)
    most_common = word_count.most_common(topn)
    most_common_dict = {word[0]: word[1] for word in most_common}
    # print(word_count)
    print(f"Total no of words: {len(words_list)}")
    print(f"Top {topn} words::")
    for word in most_common:
        print(f"{word[0]}:{word[1]}")


def count_words_numbers(file_path, topn=20):
    """
    Count all words including numbers apostrophe(') and hyphen (-)
    :param topn: Most frequent words
    :param file_path: File path for the input file
    :return:
    """
    print("COUNTING WORDS WITH NUMBERS.......")
    with open(file_path, encoding='utf-8') as in_file:
        words_list = re.findall(r"[0-9A-Za-z-']+", in_file.read())
    words_list = [word.lower() for word in words_list]
    word_count = Counter(words_list)
    most_common = word_count.most_common(topn)
    most_common_dict = {word[0]: word[1] for word in most_common}
    # print(word_count)
    print(f"Total no of words: {len(words_list)}")
    print(f"Top {topn} words::")
    for word in most_common:
        print(f"{word[0]}:{word[1]}")


if __name__ == '__main__':
    """
    Program to count words in a file
    Ignore the case
    Show the top 20 words and their occurence in the file
    """
    home = os.path.expanduser(os.getenv('USERPROFILE'))
    inp_file = fr"{home}\PycharmProjects\PythonPractice\input\sample-2mb-text-file.txt"
    inp_text = ""
    #
    with open(inp_file, "r") as file:
        for line in file.readlines():
            if not line.isspace():
                inp_text = inp_text + line + " "
    count_words(inp_text, 20)
    count_words_numbers(inp_file)
