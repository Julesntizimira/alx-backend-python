#!/usr/bin/env python3
''' The basics of async
'''


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''takes in 2 int arguments n and max_delay and
       spawn wait_random n times with the
       specified max_delay
    '''
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays
