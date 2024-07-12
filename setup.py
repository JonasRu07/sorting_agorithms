import random as rnd

def ordered_list(starting_value: int, length: int) -> list:
    """
    Creates am ordered list with a given length, beginning at a given value
    :param starting_value: first (smallest) number in the list
    :param length: How many elements there are in the list
    :return list
    """
    lst = []
    for i in range(starting_value, starting_value + length):
        lst.append(i)
    return lst


def mix(lst: list) -> list:
    """
    Takes a list and rearranges the elements in a random order
    USES AND AUXILIARY ARRAY
    :param lst: any list with any elements, only one Dimension will be shuffled
    :return: list
    """
    ret_lst = []
    for i in range(0, len(lst)):
        ret_lst.append(lst.pop(rnd.randint(0, len(lst) - 1)))

    return ret_lst#


def shuffle(lst: list) -> list:
    """
    Takes a list and shuffles the item in a random order
    :param lst: any list with any elements, only one Dimension will be shuffled
    :return: list
    """
    for i in range(1, len(lst)):
        index_element = rnd.randint(0, len(lst) - i)
        lst = lst[:index_element] + lst[index_element+1:] + [lst[index_element]]
    return lst

def is_truly_sorted(lst: list) -> bool:
    """
    Checks if a list is sorted (low to high), no doubles
    :param lst: list (only int/flt)
    :return: boolean
    """
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
    return True