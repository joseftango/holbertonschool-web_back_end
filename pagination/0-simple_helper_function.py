#!/usr/bin/env python3
"""0-simple_helper_function module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range function"""
    end: int = page * page_size
    start: int = 0
    for i in range(page - 1):
        start += page_size
    return (start, end)
