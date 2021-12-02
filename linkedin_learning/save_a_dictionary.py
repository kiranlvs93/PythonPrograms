import pickle


def save_dictionary(dictionary, outputFile):
    """
    Write a dictionary to a file
    :param dictionary:
    :param outputFile:
    :return:
    """
    with open(outputFile, 'w+') as op:
        op.write(str(dictionary))


def read_dictionary(filepath):
    """
    Read a dictionary from a file
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as inp:
        print("Read as a file::", inp.readline())


def save_dict_pickle(dictionary, outputFile_pickled):
    """
    Pickle saves the data in serialised format. Note, file is read as wb
    :param dictionary:
    :param outputFile_pickled:
    :return:
    """
    with open(outputFile_pickled, 'wb') as op:
        pickle.dump(dictionary, op)


def read_dict_pickle(outputFile_pickled):
    """
    Pickle is again used to deserialise the file data. Note, file is read as rb
    :param outputFile_pickled:
    :return:
    """
    with open(outputFile_pickled, 'rb') as ip:
        print("Pickled data::", pickle.load(ip))


if __name__ == '__main__':
    dictionary = {"Program": "Python", "Features": "Easy, fast, variety", "Founder": "Guido van Rossum"}
    op_file = r"<folderPath>\output\SampleDictionary.json"
    op_pickle_file = r"<folderPath>\output\SampleDictionary_Pickled.json"
    save_dictionary(dictionary, op_file)
    read_dictionary(op_file)
    save_dict_pickle(dictionary, op_pickle_file)
    read_dict_pickle(op_pickle_file)
