#!/usr/bin/env python3
'''define function sum_mixed_list()
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum up list elements and return the sum

    Parameters:
    - input_list (list[int | float]): The float list argument.

    Returns:
    str: The sum of list elements.
    """
    return sum(mxd_lst)
