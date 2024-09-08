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
    list_ = lst
    for i in range(0, len(list_)):
        item = list_[i]
        for j in range(0, i):
            if item < list_[j]:
                list_.remove(item)
                list_ = list_[:j] + [item] + list_[j:]
                break
    return list_


def unnamed(lst: list) -> list:
    """
    Takes an unordered list and sorts it. I don't know what alg used;
    RESEARCH NEEDED
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

def quick_sort(lst: list) -> list:
    """
    Quick sort algorithm; recursive
    :param lst: list consisting of any numbers
    :return: list
    """
    if len(lst) <= 1:
        return lst
    else:
        return_list = []
        slice_a = quick_sort(lst[:int(len(lst)/2)])
        slice_b = quick_sort(lst[int(len(lst)/2):])

        while len(slice_a) > 0 and len(slice_b) > 0:
            if slice_a[0] < slice_b[0]:
                return_list.append(slice_a.pop(0))
            else:
                return_list.append(slice_b.pop(0))

        if len(slice_a) == 0:
            return_list = return_list + slice_b
        else:
            return_list = return_list + slice_a
        return return_list
