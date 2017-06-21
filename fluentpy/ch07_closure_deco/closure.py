#!/usr/bin/env python
# encoding: utf-8

"""
@description: 闭包

@author: BaoQiang
@time: 2017/6/14 10:19
"""

import functools
from functools import singledispatch

from collections import abc
import numbers
import html

b = 1


def var_scope():
    global b
    print(b)
    b = 2


def make_average():
    series = []

    def averager(new_val):
        series.append(new_val)
        total = sum(series)
        return total / len(series)

    return averager


def make_average2():
    total = 0
    count = 0

    def averager(new_val):
        nonlocal total, count
        count += 1
        total += new_val
        return total / count

    return averager


# 缓存相同结果的函数调用实例
@functools.lru_cache(maxsize=256, typed=False)
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


def closure_demo():
    avg = make_average2()
    print(avg(1))
    print(avg(2))
    print(avg(3))


# 不同的函数功能的应用分发

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<li>\n</li>'.join(htmlize(item) for item in seq)
    return '<ul>\n</ll>' + inner + '<li>\n</ul>'


def htmlize_demo():
    print(htmlize([1, 'a', 2]))


def main():
    # closure_demo()
    htmlize_demo()


if __name__ == '__main__':
    main()
