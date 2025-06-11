#!/usr/bin/env python3
"""101-safly_get_value module"""
from typing import TypeVar, Any, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    '''safly get value form dict argument'''
    if key in dct:
        return dct[key]
    else:
        return default
