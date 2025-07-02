#!/usr/bin/env python3
"""0-async_generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() ->  AsyncGenerator:
    """asynchronous generator function that
    yields random float in each iteration"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
