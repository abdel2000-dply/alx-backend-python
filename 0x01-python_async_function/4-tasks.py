#!/usr/bin/env python3
''' task_wait_n '''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' spawn wait_random n times with the specified max_delay'''
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)
