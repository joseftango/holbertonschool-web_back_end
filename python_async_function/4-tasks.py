#!/usr/bin/env python3
'''4-tasks module'''
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''takes an integer and return asyncio.Task object'''
    tasks: typing.List[asyncio.Task] = \
        [task_wait_random(max_delay) for t in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
