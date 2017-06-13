#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数式编程

@author: BaoQiang
@time: 2017/6/13 20:25
"""

from functools import reduce
from operator import mul
from operator import itemgetter, attrgetter
from collections import namedtuple
from operator import methodcaller

Person = namedtuple('Person', ('name', 'age'))


def fact(n):
    return reduce(mul, range(1, n + 1))


def item_get():
    data = [
        (1, 'a'),
        (2, 'b')
    ]

    data.sort(key=itemgetter(1), reverse=True)
    print(data)

    data2 = [
        Person('xiao', 13),
        Person('bao', 14)
    ]

    data2.sort(key=attrgetter('age'), reverse=True)
    print(data2)


def method_call():
    txt = 'hello world'
    new_replace = methodcaller('replace', ' ', '-')
    print(new_replace(txt))


def func_demo():
    # print(fact(4))
    # item_get()
    method_call()


def main():
    func_demo()


if __name__ == '__main__':
    main()
