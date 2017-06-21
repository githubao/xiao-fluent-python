#!/usr/bin/env python
# encoding: utf-8

"""
@description: 生成器组合

@author: BaoQiang
@time: 2017/6/19 15:02
"""


def chain_old(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain_new(*iterables):
    for i in iterables:
        yield from i


def iterfrom_run():
    s = 'abc'
    t = tuple(range(3))
    print(list(chain_old(s, t)))
    print(list(chain_new(s, t)))


def main():
    iterfrom_run()


if __name__ == '__main__':
    main()
