#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现一个python典型类

@author: BaoQiang
@time: 2017/6/14 14:25
"""

from array import array
import math


class Vector2D:
    typecode = 'd'

    # 只有这两个属性，不能再有添加新的属性的能力
    # 主要是为了优化内存，提高存取速率
    # __slots__ 不能被继承
    __slots__ = ['_x', '_y']

    """
    _x 表示私有的
    __x 会被改名为_Vector2D__x，防止继承的子类意外修改
    """

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        """
        把属性变成只读的
        :return: 
        """
        return self._x

    @property
    def y(self):
        return self._y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format2__(self, format_spec):
        """
        整数： bcdoxXn
        浮点数： eEfFgGn%
        字符串： s
        :param format_spec: 
        :return: 
        """
        components = (format(c, format_spec) for c in self)
        return '({} {})'.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

class ShortVector2D(Vector2D):
    typecode = 'f'

def fmt_demo():
    print(format(42, 'b'))
    print(format(2 / 3, '.1%'))

    from datetime import datetime
    now = datetime.now()
    print(format(now, '%H:%M:%S'))
    print(format(now, 'it\'s now {:%I:%M %p}'))


def vec_cls():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(5, 12)
    print({v1, v2})

    print(format(v1, '0.2fp'))


def main():
    # fmt_demo()
    vec_cls()


if __name__ == '__main__':
    main()
