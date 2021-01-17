#!/usr/bin/env python
# -*- coding: utf-8 -*-

def map_funcation(fun_map, *iterators):
    """
    customize high-order function map
    """
    try:
        i = 0
        while 1:
            yield fun_map(*[j[i] for j in iterators])
            i += 1
    except IndexError:
        pass


if __name__ == "__main__":
    data_list = [1, 3, 5, 6]
    result = map_funcation(lambda x, y: x + y, data_list, data_list)
    print(list(result))
