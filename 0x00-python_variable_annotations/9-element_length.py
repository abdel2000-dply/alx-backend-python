#!/usr/bin/env python3
''' Element Length Module '''
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    ''' Returns a list of tuples containing elements and their length '''
    return [(i, len(i)) for i in lst]
