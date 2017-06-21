#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/6/19 15:03
"""

import itertools


def iterator_func():
    """
    compress((a,b,c),(1,0,1)) = (a,c)
    dropwhile
    filter
    filterfalse
    islice
    takewhile

    accumulate: 截止到目前为止，把前面的所有元素应用到第二个参数func，然后依次输出结果
    enumerate
    map
    startmap

    chain
    chain.from_iteratable
    product: 计算笛卡尔乘积，两两对应相乘组合
    zip: zip_longest

    combinations
    combinations_with_replacement
    count
    cycle
    permutations
    repeat

    groupby
    reversed
    tee: 两个相同的迭代器，分别用于迭代互不影响

    :return: 
    """


def itertools_run():
    gen = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2))
    print(list(gen))


def main():
    itertools_run()


if __name__ == '__main__':
    main()
