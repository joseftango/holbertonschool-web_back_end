#!/usr/bin/env python3
"""8-make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function make_multiplier"""

    def multiplier_function(x: float) -> float:
        """function multiplier_function"""
        return x * multiplier
    return multiplier_function
