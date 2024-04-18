#!/usr/bin/env python3
''' Module '''
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' safe_first_element: returns the first element of a list '''
    if lst:
        return lst[0]
    else:
        return None
