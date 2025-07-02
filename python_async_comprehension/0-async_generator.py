#!/usr/bin/env python3
"""0-async_generator"""
import asyncio
import random


async def async_generator():
    """asynchronous generator function that
    yields random float in each iteration"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
