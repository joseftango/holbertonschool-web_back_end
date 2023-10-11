#!/usr/bin/env python3
"""6-sum_mixed_list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to sum a list of mixed integers and floats."""
    total = 0.0
    for x in mxd_lst:
        total += float(x)
    return total
