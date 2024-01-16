#!/usr/bin/env python3
'''Async Generator
'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''return asynchronous generator
    '''
    for _ in range(10):
        number = uniform(0, 10)
        await asyncio.sleep(1)
        yield number
