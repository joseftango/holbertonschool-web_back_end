#!/usr/bin/env python3
"""9-element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function named element_length"""
    return [(i, len(i)) for i in lst]
