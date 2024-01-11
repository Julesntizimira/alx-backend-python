#!/usr/bin/env python3
'''define function zoom_array()
'''
from typing import Tuple, List, Any, Optional


def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    ''' validate the following piece of code and apply any necessary changes'''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)