# SPDX-FileCopyrightText: 2022 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations


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


def print_hello():
    print("hello!")


def sum_product(lists):
    def print_hello():
        print("hello!")

    product = 1.0
    for item in lists:
        product *= item
    return product
