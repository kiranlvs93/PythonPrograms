def sort_a_string(inp):
    """
    Function to return the sorted words in a string
    The words are sorted by ignoring the case
    When the result is returned, the original case should be preserved
    :param inp:
    :return:
    """
    words = inp.split()
    # Dictionary to save the original case
    original = {word.lower(): word for word in words}
    # Convert all the words to lower case to ignore the case sensitivity
    words = [word.lower() for word in words]
    words.sort()
    return [original[word] for word in words]


if __name__ == '__main__':
    print("Enter any string to sort them or enter quit to exit")
    while True:
        user_inp = input(">>>")
        if user_inp != 'quit':
            print(sort_a_string(user_inp))
        else:
            break
