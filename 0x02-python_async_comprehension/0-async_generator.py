#!/usr/bin/python3
''' Async Generator '''
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    ''' Async Generator '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
