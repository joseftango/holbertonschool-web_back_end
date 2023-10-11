#!/usr/bin/env python3
"""0-basic_async_syntax module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random"""
    delay = random.uniform(0, float(max_delay))

    await asyncio.sleep(delay)
    return delay
