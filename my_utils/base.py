from itertools import chain


def flatten(lst):
    """
    Given a list of lists, this concatenates all the sublists into a single one and returns it.
    :param lst: List of lists
    :return: List
    """
    return list(chain.from_iterable(lst))

