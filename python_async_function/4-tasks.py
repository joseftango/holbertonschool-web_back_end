#!/usr/bin/env python3
"""4-tasks"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """wait_random"""
    delay = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
