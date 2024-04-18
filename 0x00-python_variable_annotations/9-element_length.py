#!/usr/bin/env python3
''' Element Length Module '''
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns a list of tuples containing elements and their length '''
    return [(i, len(i)) for i in lst]
