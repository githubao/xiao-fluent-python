#!/usr/bin/env python
# encoding: utf-8

"""
@description: memory view

@author: BaoQiang
@time: 2017/6/12 11:45
"""

import array
import heapq


def memoryview_run():
    """
    -2
    [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
    array('h', [-2, -1, 1024, 1, 2])
    :return: 
    """
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(memv[0])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)


def heapq_run():
    lst = []
    heapq.heappush(lst, 3)
    heapq.heappush(lst, 2)
    heapq.heappush(lst, 1)
    heapq.heappush(lst, 4)
    print(heapq.heappop(lst))
    print(heapq.nlargest(2, lst))


def main():
    # memoryview_run()
    heapq_run()


if __name__ == '__main__':
    main()
