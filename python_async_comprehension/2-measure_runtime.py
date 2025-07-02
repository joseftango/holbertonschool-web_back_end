#!/usr/bin/env python3
"""2-measure_runtime module"""
from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures runtime of an async function
    that executes four times concorrently'''
    tasks = [async_comprehension(),
             async_comprehension(), async_comprehension()]
    start = time()
    res = await gather(*tasks)
    end = time()
    runtime = end - start
    return runtime
