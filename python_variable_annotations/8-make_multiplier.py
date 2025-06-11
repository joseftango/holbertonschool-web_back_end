#!/usr/bin/env python3
"""7-to_kv module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    x: float = 2.22
    return lambda multiplier: x*multiplier
