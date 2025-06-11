#!/usr/bin/env python3
"""100-safe_first_element module"""
from typing import Iterable, Sequence, Tuple, List, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
