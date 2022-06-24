# SPDX-FileCopyrightText: 2022 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0

# comment
def sum_function(list):
    """
    A function which takes a list as an argument and
    returns the sum

    Parameters
    ----------
    list: list
        Must be floats or ints

    Returns
    -------
    float:
        The sum of the elements in list
    """
    sum = 0.0
    for item in list:
        sum += item
    return sum


def sum_product(list):
    product = 1.0
    for item in list:
        product *= item
    return product


def square_array(list):
    return [item*item for item in list]


def make_author_print(author="Guillermo"):
    """This function makes a print of the author of this change
    This should be made with spaces now
    """
    print("Guillermo Made a fork")
