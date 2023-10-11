#!/usr/bin/env python3
"""3-tasks"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """task_wait_random function"""
    task = wait_random(max_delay)
    result = asyncio.ensure_future(task)
    return result
