from functools import reduce


def unique_items(list1):

    # Print directly by using * symbol
    unique_list = reduce(lambda re, x: re + [x] if x not in re else re, list1, [])
    return unique_list
