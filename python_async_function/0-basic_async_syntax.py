#!/usr/bin/env python3
'''0-basic_async_syntax module'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and max_delay then '''
    rand_pause = random.uniform(0, max_delay)
    await asyncio.sleep(rand_pause)
    return rand_pause
