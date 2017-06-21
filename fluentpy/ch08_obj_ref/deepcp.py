#!/usr/bin/env python
# encoding: utf-8

"""
@description: 深复制 和 浅复制

@author: BaoQiang
@time: 2017/6/14 12:42
"""

import weakref
from weakref import WeakKeyDictionary, WeakSet
from copy import deepcopy,copy

def loop_ref():
    a = [1, 2]
    b = [a, 3]
    a.append(b)
    print(a)
    print(a[2][0])


def weakref_demo():
    """
    弱引用不会增加引用计数，即使对象只有被弱引用引用，也会被回收
    :return: 
    """
    s1 = {1, 2, 3}
    s2 = s1

    def bye():
        pass

    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 3
    print(ender.alive)


def eq_ne():
    # Cpython 的特殊优化措施
    # t1 = (1, 2, 3)
    # t2 = tuple(t1)
    # t3 = t1[:]
    # print(t1 is t2)
    # print(t1 is t3)
    #
    # t4 = (1,2,3)
    # t5 = (1,2,3)
    # print(t4 is t5)
    #
    # # 共享字符串字面量
    # s1 = 'abc'
    # s2 = 'abc'
    # print(s1 is s2)

    # frozenset 不可序列化，返回的是相同的对象
    # fz1 = frozenset({1,2})
    # # fz2 = fz1[:]
    # fz3 = copy(fz1)
    # # print(fz1 is fz2)
    # print(fz1 is fz3)

    i1 = int(333444444)
    i2 = int(333444444)
    print(i1 is i2)

def main():
    # loop_ref()
    # weakref_demo()
    eq_ne()


if __name__ == '__main__':
    main()
