#!/usr/bin/env python3
'''0-basic_async_syntax module'''
from random import uniform
from asyncio import sleep


async def wait_random(max_delay=10):
    '''waits for a random delay between 0 and max_delay then '''
    rand_pause = uniform(0, max_delay)
    await sleep(rand_pause)
    return rand_pause
