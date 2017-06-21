#!/usr/bin/env python
# encoding: utf-8

"""
@description: 元组拆包

@author: BaoQiang
@time: 2017/6/9 18:48
"""

from collections import namedtuple


def naming():
    Person = namedtuple('Person', ('name', 'age'))
    xiao = ('xiao', 17)
    p = Person._make(xiao)
    p2 = Person('xiao', 17)
    print(p)
    print(p2)
    print(p._asdict())


def unpack():
    """
    {:填充(默认是空格)<(左对齐)^(居中对齐)>(右对齐)位数}
    {:b(二进制)d(十进制)o(八进制)x(十六进制)}
    :return: 
    """
    print('|{:15}|{:^9}|{:9.4f}|'.format('', 'hh', 34.4351348))
    print('{:,}'.format(2325353212))


class Test:
    def __init__(self, p):
        self.p = p

    # 会无限递归
    # def __getattribute__(self, item):
    #     return self.p

    # 调用父类的 __getattribute__ 方法
    # def __getattribute__(self, item):
    #     return super().__getattribute__(item)

    # 实现的时候，如果不调用 __getattribute__, 需要手动调用 __getattr__
    # def __getattribute__(self, item):
    #     print(111)
    #     # 因为这一句会抛出AttributeError，所以会调用 __getattr__
    #     return super().__getattribute__(item)

    def __getattribute__(self, item):
        print(222)

    def __getattr__(self, item):
        return 'default'


def increase():
    """
    实现就地加法，性能更好
    :return: 
    """
    lst = [1, 3]
    print(id(lst))
    lst *= 2
    print(id(lst))


def test():
    t = Test(4)
    # print(t.p)
    print(t.no_exists)


def main():
    # unpack()
    # naming()
    # test()
    increase()


if __name__ == '__main__':
    main()
