#!/usr/bin/env python3
"""1-concurrent_coroutines module"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''spawn wait_random n times with the specified max_delay.'''
    call_n_time: typing.List[typing.Coroutine]
    results: typing.List[float]

    for i in range(n):
        call_n_time.append(wait_random(max_delay))

    results = await asyncio.gather(*call_n_time)
    return results
