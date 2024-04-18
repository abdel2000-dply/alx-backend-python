#!/usr/bin/env python3
''' to_kv module'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Return a tuple with a string and a float '''
    return (k, v * v)
