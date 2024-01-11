#!/usr/bin/env python3
'''define function safe_first_element()
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    takes a sequence and return Any

    Parameters:
    - lst (Sequence): the argument

    Returns:
    Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
