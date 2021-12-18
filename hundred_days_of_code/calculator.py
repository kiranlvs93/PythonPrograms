"""
A cool calculator that performs basic operations like +/*-%.
It stores the previous results and lets you perform further operations.
Check for exceptions like division error etc. Once the result is None, calculator is reset by showing it to the user
"""
import utilities.cmd_operations as utils
import utilities.ascii_art as art


def result(a, b, op):
    """
    Takes the numbers and returns the result be performing one of the given operations
    :param a:
    :param b:
    :param op:
    :return:
    """
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b
        else:
            print("Invalid operand. Please chose one among these:: + - / * %")
            return
    except Exception as ex:
        print(f"Unable to perform the operation. Error:: {ex}")
        return None


def choose_operand():
    """
    Chooses an operand. If user enters an invalid operand, it asks for a correct one in recursion.
    :return:
    """
    operand = input("Pick an operation: + - / * %::")
    if operand in "+-/*%":
        return operand
    else:
        print("Invalid operation")
        return choose_operand()


def calculator():
    print(art.calc_logo)
    x = float(input("What's your first number::"))
    while True:
        operation = choose_operand()
        y = float(input("What's your second number::"))
        res = result(x, y, operation)
        print(f"{x} {operation} {y} = {res}")
        if res is not None:
            cont = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation:")
            if cont == 'y':
                x = res
            elif cont == 'n':
                utils.clear()
                calculator()
            else:
                print("Invalid operation")
                break
        else:
            input("Result is None. Restarting the calculator....")
            utils.clear()
            calculator()


calculator()
