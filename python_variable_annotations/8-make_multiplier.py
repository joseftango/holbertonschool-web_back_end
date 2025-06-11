#!/usr/bin/env python3
"""7-to_kv module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier"""
    x: float = 2.22
    return lambda multiplier: x*multiplier
