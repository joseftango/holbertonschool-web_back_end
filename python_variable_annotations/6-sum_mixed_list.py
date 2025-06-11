#!/usr/bin/env python3
"""6-sum_mixed_list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''calculates the sum of all int or float items in list'''
    return sum(mxd_lst)
