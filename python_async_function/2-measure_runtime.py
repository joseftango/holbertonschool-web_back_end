#!/usr/bin/env python3
"""2-measure_runtime module"""
import asyncio
import typing
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution"""
    start: float = time.time()
    res: typing.List[float] = asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    total_time: float = end - start

    return total_time / n
