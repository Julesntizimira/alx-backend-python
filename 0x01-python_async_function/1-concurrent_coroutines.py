#!/usr/bin/env python3
''' The basics of async
'''
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''takes in 2 int arguments n and max_delay and
       spawn wait_random n times with the
       specified max_delay
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
