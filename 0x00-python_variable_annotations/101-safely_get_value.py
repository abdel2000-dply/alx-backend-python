#!/usr/bin/env python3
''' Module '''
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    ''' Return value of key if it exists, otherwise return default '''
    if key in dct:
        return dct[key]
    else:
        return default
