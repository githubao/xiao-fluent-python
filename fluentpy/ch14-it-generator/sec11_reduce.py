#!/usr/bin/env python
# encoding: utf-8

"""
@description: 规约函数 reduce

@author: BaoQiang
@time: 2017/6/19 15:18
"""

from random import randint


def reduce_run():
    """
    all
    any
    max
    min
    reduce
    sum
    sorted
    
    :return: 
    """


def rand():
    return randint(1, 6)


def iter_sentinel():
    "哨兵值"
    rand_iter = iter(rand, 1)
    print(list(rand_iter))

    with open('somefile.dat') as fp:
        for line in iter(fp.readline, '\n'):
            """
            process line
            """


def main():
    iter_sentinel()


if __name__ == '__main__':
    main()
