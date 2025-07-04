#!/usr/bin/env python3
"""0-async_generator module"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''coroutine will collect 10 random numbers using
    an async comprehensing over async_generator'''
    result = []
    async for n in async_generator():
        result.append(n)
    return result
