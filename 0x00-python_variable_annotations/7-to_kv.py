#!/usr/bin/env python3
'''define function to_kv()
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    build a tuple from two arguments

    Parameters:
    - k (str): The first argument.
    - v (int | float): the second argument.

    Returns:
    tuple: tuple built from the arguments
    """
    return (k, v)
