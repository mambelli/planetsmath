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


def sum_product(list):
    product = 1.0
    for item in list:
        product *= item
    return product


def multiply_by_2(list):
    product = 1.0
    for item in list:
        product *= 2
    return product


def division_function(list):
    division = 1.0
    for item in list:
        division /= item
    return division
