#!/usr/bin/env python3
'''define function sum_list()
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum up list elements and return the sum

    Parameters:
    - input_list (list[float]): The float list argument.

    Returns:
    str: The sum of list elements.
    """
    return sum(input_list)
