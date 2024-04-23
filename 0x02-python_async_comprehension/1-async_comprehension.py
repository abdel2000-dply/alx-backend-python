#!/usr/bin/env python3
''' Async Comprehensions '''
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    ''' Async Comprehensions '''
    return [n async for n in async_generator()]
