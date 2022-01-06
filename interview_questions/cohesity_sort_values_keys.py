def solution(scores):
    """
    The marketing team at CodeSignal would like to know how many users there are in each Coding Score range for
    standardized tests like the General Coding Assessment, so that they can share that information on our website.
    They've asked you to create a report containing that information Your Mission As input, you are given a list of
    scores Coding Score can be anywhere between 300 and 850. For the purpose of this task, levels are defined in the
    following way. Poor: 300-599 Fair: 600-699 Good: 700-749 Excellent: 750-799 Elite: 800 Calculate how many users
    are there in each level, then return a list of strings where each string represents a level and the number of
    users who fall within that range formatted like LevelName: count should be displayed. Levels should be sorted in
    decreasing order of those numbers, omitting any levels that have no users. In case of a tie the higher level
    should appear first. For example, if you had this input... [330, 723, 730, 825] ...then you should return the
    following: [ Good: 2', Elite: 1', Poor: 1 ] [execution time limit] 4 seconds (py3) • [input]
    array.integer scores An array of integers in the range [300, 850] [output] array.string An array of strings
    formatted like LevelName: count
    :param scores:
    :return:
    """
    user_levels = {}
    user_levels_sorted = {}
    # Find the count of scores in each rank
    for score in scores:
        # Appending 1,2,3,4,5 to sort them later in ascending order
        if score >= 800:
            user_levels['1Elite'] = user_levels.get('1Elite', 0) + 1
        elif score >= 750:
            user_levels['2Excellent'] = user_levels.get('2Excellent', 0) + 1
        elif score >= 700:
            user_levels['3Good'] = user_levels.get('3Good', 0) + 1
        elif score >= 600:
            user_levels['4Fair'] = user_levels.get('4Fair', 0) + 1
        elif score >= 300:
            user_levels['5Poor'] = user_levels.get('5Poor', 0) + 1

    # Sort based on values first and then on keys using SORTED function
    user_levels_sorted = dict(sorted(user_levels.items(), key=lambda x: (-x[1], x[0])))
    output = []

    # Concatenate the keys and values from sorted dictionary and append them to a list
    for k, v in user_levels_sorted.items():
        output.append(k[1:] + ' - ' + str(v))
    print(output)
    return output


solution([330, 723, 730, 825, 780, 770, 790])
# solution([463, 520, 364, 844, 741, 645, 744, 768, 605, 616])
# solution([788, 746, 488, 729, 802, 403, 588, 834, 448, 701, 579, 358, 496, 630, 788, 591, 666, 665, 517, 688, 443, 757, 397, 531, 735, 705, 768, 759, 342, 460])
# solution([463, 745, 470, 835, 495, 371, 799, 475, 518, 812, 693, 535, 435, 570, 799, 560, 767, 352, 467, 434, 486, 428, 633, 362, 401, 407, 334, 823, 808, 406])
# solution([708, 334, 518, 420, 661, 456, 332, 486, 438, 533, 492, 668, 396, 586, 475, 643, 745, 317, 753, 480, 405, 787, 650, 719, 562, 839, 635, 449, 534, 554])
