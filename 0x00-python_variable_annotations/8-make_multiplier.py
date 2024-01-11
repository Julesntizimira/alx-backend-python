#!/usr/bin/env python3
'''define function make_multiplier()
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    sum up list elements and return the sum

    Parameters:
    - input_list (list[int | float]): The float list argument.

    Returns:
    str: The sum of list elements.
    """
    def mult(to_mult: float):
        return multiplier * to_mult
    return mult
