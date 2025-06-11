#!/usr/bin/env python3
"""9-element_length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''annotate function's parameters and
    return values with the appropriate types'''
    return [(i, len(i)) for i in lst]
