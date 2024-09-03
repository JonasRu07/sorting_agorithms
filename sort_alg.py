"""
Module with different sorting algorithms
they are either based on theoretical algorithms(named after
that theory), or based on feeling

"""

def insertion(lst: list) -> list:
    """
    Takes an unordered list and sorts it via an insertion sort inspired algorithm.
    It currently only works with only number-lists
    :param lst: a list out of numbers (int and/or flt)
    :return: list
    """
    sorting = True
    while sorting:
        sorting = False
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i+1]:
                try:
                    lst = lst[:i] + [lst[i+1]] + [lst[i]] + lst[i+2:]
                except IndexError:
                    lst = lst[:i] + [lst[i + 1]] + [lst[i]]
                sorting = True
    return lst


def last_sort(lst: list) -> list:
    """
    Takes an unordered list and sorts it.
    It currently only works with only number-lists
    :param lst: a list out of numbers (int and/or flt)
    :return: list
    """
    a = lst[0]
    for n in range(0, len(lst)):
        for i in range(len(lst) - n):
            if a > lst[i]:
                a = lst[i]
        lst.remove(a)
        lst.append(a)
        a = lst[0]
    return lst
