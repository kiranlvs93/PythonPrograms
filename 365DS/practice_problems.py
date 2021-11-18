def int_to_string():
    """
    Write code that asks the user to input a number between 1 and 5 inclusive. The code will take the integer value and
    print out the string value. So for the example if the user inputs 2 the code will print two. Reject any input that
    is not a number in that range
    """
    print("Enter a number b/w 1 and 5. Enter 0 to exit")
    while True:
        try:
            num = int(input(">>>"))
            if num == 1:
                print("One")
            elif num == 2:
                print("Two")
            elif num == 3:
                print("Three")
            elif num == 4:
                print("Four")
            elif num == 5:
                print("Five")
            elif num == 0:
                print("Quit")
                break
            else:
                print("Out of range")
        except:
            print("Invalid number. Don't enter strings")


def question3():
    """
    Question 3
    Create a variable containing an integer between 1 and 10 inclusive. Ask the
    user to guess the number. If they guess too high or too low, tell them they
    have not won. Tell them they win if they guess the correct number.
    :return:
    """


def question4():
    """
    Question 4
    Ask the user to input their name. Check the length of the name. If it is
    greater than 5 characters long, write a message telling them how many characters
    otherwise write a message saying the length of their name is a secret
    :return:
    """


def question5():
    """
    Question 5
    Ask the user for two integers between 1 and 20. If they are both greater than
    15 return their product. If only one is greater than 15 return their sum, if
    neither are greater than 15 return zero
    :return:
    """


def question5():
    """
    Question 6
    Ask the user for two integers, then swap the contents of the variables. So if
    var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
    and var_2 should equal 1.
    :return:
    """
    a, b = input("Enter 2 nos separated by space\n>>>").split(' ')
    print('First no: %s \nSecond no: %s' % (a, b))
    b, a = a, b
    print('After swapping')
    print('First no: %s \nSecond no: %s' % (a, b))


def bubble_sort():
    my_list = [53, 76, 25, 98, 56, 42, 69, 81]
    my_list_copy = my_list.copy()
    for i in range(len(my_list)):
        print("Outer Iteration ", i + 1)
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            print(j, ':', my_list)
        print('**********************')
    print("Sorted::", my_list)
    print("Sorted using BIF:", sorted(my_list_copy))


if __name__ == '__main__':
    # int_to_string()
    # question5()
    bubble_sort()
