import itertools


def two_sum(inp_list, desired_sum):
    """
    Question - FRom the given list of numbers, find the indices of the numbers that sum to a target number.
    E.g - inp = [2, 5, 3, 7, 4], target = 10, result = [2,3]
    Find all possible combinations of the list. Check if the combination sums to desired target. If yes, then return the
    indices of those numbers
    :param inp_list:
    :param desired_sum:
    :return:
    """
    desired_indices = []
    for comb in itertools.combinations(inp_list, 2):
        if sum(comb) == desired_sum:
            desired_indices.append((inp_list.index(comb[0]), inp_list.index(comb[1])))
    return desired_indices if len(desired_indices) > 0 else -1


def two_sum_logic2(inp_list, desired_sum):
    """
    Iterate through the loop and then for each number find the number required to make the sum
    i.e num_req = target - curr_num. If this number is there in the list at any position other than the
    current position then return the index of the current iteration as that's the index of curr number and the index
    of the num_req. Else, return -1
    :param inp_list:
    :param desired_sum:
    :return:
    """
    for i in range(len(inp_list)):
        no_req = desired_sum - inp_list[i]
        if no_req in inp_list and inp_list.index(no_req) != i:
            return [i, inp_list.index(no_req)]
    return -1


def brackets_balance(inp_str):
    brackets_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    if len(inp_str) % 2 != 0:
        print("Length is odd")
        return -1
    else:
        print('Length is even. Proceeding with validation....')
        count = 1
        for i in range(len(inp_str) // 2):
            print(brackets_dict.get(inp_str[i]), inp_str[-count])
            if brackets_dict.get(inp_str[i]) != inp_str[-count]:
                return -1
            count += 1
    return 1


def linear_search(items, element):
    for item in items:
        if item == element:
            return f"Element {element} found at position {items.index(element)}"
    return f"Element {element} not found"


def binary_search(items, ele):
    items.sort()
    print(f"Items after sorting {items}")
    found = False
    low = 0
    high = len(items) - 1

    while not found and low <= high:
        mid = round((low + high) / 2)
        if ele == items[mid]:
            return f"Element {ele} found"
        elif ele > items[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return f"Element {ele} not found"


def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j - 1] > items[j]:
                items.insert(j - 1, items.pop(j))
            else:
                break
    return items


def luhns_algorithm(card_number):
    """
    Luhn's algorithm tells us whether the given credit card number is valid or not. The algorithm is as follows:
    1. Multiply every second digit by 2 starting from the 2nd to last
    2. add those digits together
    3. Add that number to the sum of digits that weren't multiplied by 2
    4. If the remainder is 0 after the above sum is divided by 10, then it s a valid Credit Card Number

    num = 371449635398431
    1: all nos in ()*2 - 3(7)1(4)4(9)6(3)5(3)9(8)4(3)1 = 14,8,18,6,6,16,6
    2: 1+4+8+1+8+6+6+1+6+6 = 47
    3: Sum = 47+3+1+4+6+5+9+4+1 = 80
    4: 80%10 ==0 -> Valid card number
    :param card_number:
    :return:
    """
    crd_no = list(card_number)
    sum_alt_digits = 0
    sum_other_digits = 0
    # Iterate from the last 2nd digit to first digit
    # for i in range(len(crd_no) - 2, 0, 2):
    i: int
    for i in range(len(crd_no)):
        if i % 2 != 0:
            # Multiply every second digit by 2
            pdt = 2 * int(crd_no[i])
            # Add those digits together
            sum_alt_digits += sum(int(ch) for ch in str(pdt))
        else:
            sum_other_digits += int(crd_no[i])

    # sum_other_digits = sum([int(ch) for ch in crd_no])
    print(f'{sum_alt_digits}+{sum_other_digits} = {sum_alt_digits + sum_other_digits}')
    if (sum_alt_digits + sum_other_digits) % 10 == 0:
        return "Valid credit card number"
    else:
        return "Invalid credit card number"


def coins(num_of_coins):
    coins_array = [True] * num_of_coins

    for i in range(1, num_of_coins):
        # print('*********************')
        # print(f'i={i}')
        for j in range(i, num_of_coins):
            # print(f'j={j}')
            if (j+1) % (i+1) == 0:
                # print(f'Flipping coin at {j}')
                coins_array[j] = not coins_array[j]
    print(f'No of heads after flipping all coins: {coins_array.count(True)}')


if __name__ == '__main__':
    # print(two_sum([2, 5, 3, 7, 4], 10))
    # print(two_sum_logic2([2, 5, 3, 7, 4], 10))
    # print(two_sum_logic2([8, 6 , 11, 3], 9))
    # print(brackets_balance('[({)})]'))
    # print(linear_search([10, 2, 35, 44, 5], 35))
    # print(linear_search([10, 2, 35, 44, 5], 100))
    # print(binary_search([10, 2, 35, 44, 5, 6], 44))
    # print(binary_search([6, 5, 8, 2, 3, 87, 24, 70], 100))
    # print(insertion_sort([3, 2, 7, 5, 15, 9, 12]))
    # print(insertion_sort([70, 24, 87, 45, 6, 3, 2, 8, 5]))
    # print(luhns_algorithm('371449635398431'))
    # print(luhns_algorithm('4386280036972366'))
    coins(1001)