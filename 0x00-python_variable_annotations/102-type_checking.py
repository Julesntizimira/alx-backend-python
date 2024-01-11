#!/usr/bin/env python3
'''define function zoom_array()
'''
from typing import Tuple, List, Any, Optional, Sequence, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    takes a sequence and return Any

    Parameters:
    - lst (Sequence): the argument

    Returns:
    Any or None
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
