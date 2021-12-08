import os
import random, secrets


def generate_passphrase(no_of_passphrase):
    """
    Generating a passphrase by simulating a dice
    Each passphrase need 5 rolls
    Simulating dice using random module
    :param no_of_passphrase:
    :return:
    """
    # Each pass phrase need 5 rolls. So total rolls is as below
    home = os.path.expanduser(os.getenv('USERPROFILE'))
    diceware_file = fr"{home}\PycharmProjects\PythonPractice\input\diceware_list.txt"
    final_pass_phrase = []
    word_list = dict()
    # Storing the diceware words into a  dictionary
    with open(diceware_file, encoding='utf-8') as file:
        for line in file.readlines():
            word_list[line.split()[0]] = line.split()[1]

    # Generating the pass phrase
    for _ in range(no_of_passphrase):
        phrase_number = ''
        for _ in range(5):
            phrase_number = phrase_number + str(random.randint(1, 6))
        final_pass_phrase.append(word_list[phrase_number])
    return " ".join(final_pass_phrase)


def generate_passphrase_secrets(no_of_passphrase):
    """
    Generating passphrase using secrets, the recommended module for encryption
    :param no_of_passphrase:
    :return:
    """
    home = os.path.expanduser(os.getenv('USERPROFILE'))
    diceware_file = fr"{home}\PycharmProjects\PythonPractice\input\diceware_list.txt"
    with open(diceware_file, encoding='utf-8') as file:
        word_list = [line.split()[1] for line in file.readlines()]
    return " ".join([secrets.choice(word_list) for _ in range(no_of_passphrase)])


if __name__ == '__main__':
    print(generate_passphrase(5))
    print(generate_passphrase_secrets(5))
