
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