#!/usr/bin/env python3
"""1-concat"""


def floor(n: float) -> int:
    """returns the largest integer less
    than or equal to a given number"""
    if n >= 0:
        return int(n)
    else:
        return int(n) - (n != int(n))
