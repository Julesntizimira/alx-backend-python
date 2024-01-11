#!/usr/bin/env python3
'''define function safe_first_element()
'''
from typing import Union, TypeVar, Optional, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    takes a sequence and return Any

    Parameters:
    - lst (Sequence): the argument

    Returns:
    Any or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
