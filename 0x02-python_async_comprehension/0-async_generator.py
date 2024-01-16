#!/usr/bin/env python3
'''Async Generator
'''
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''return asynchronous generator
    '''
    for _ in range(10):
        number = uniform(0, 10)
        await asyncio.sleep(1)
        yield number
