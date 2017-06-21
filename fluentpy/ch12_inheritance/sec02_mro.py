#!/usr/bin/env python
# encoding: utf-8

"""
@description: mro demo

@author: BaoQiang
@time: 2017/6/17 11:21
"""

import numbers
import io

def print_mro(cls):
    print(', '.join(c.__name__ for c in cls.__mro__))

def mro_run():
    print_mro(bool)
    print_mro(numbers.Integral)
    print_mro(io.TextIOBase)
    print_mro(io.TextIOWrapper)


def main():
    mro_run()


if __name__ == '__main__':
    main()