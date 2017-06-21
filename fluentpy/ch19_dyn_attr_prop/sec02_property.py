#!/usr/bin/env python
# encoding: utf-8

"""
@description: 属性验证的逻辑

@author: BaoQiang
@time: 2017/6/21 19:56
"""


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.weight = value
        else:
            raise ValueError('value must be > 0')


class Foo():

    # 如果定义了 __slots__，那么类没有 __dict__ 属性，而且属性值 只由slot的元组组成
    __slots__ = ()

    @property
    def pro(self):
        return 'pro'


def run():
    f = Foo()
    print(f.pro)

    """
    err
    """
    # f.pro = 'new1'

    """
    使得pro变得不再是property
    """
    Foo.pro = 'new2'

    print(f.pro)
    print(Foo.pro)

    """
    property 是 覆盖型 描述符，
    """


# 属性的设置工厂方法
def quantity(storage_name):
    def qty_getter(ins):
        return ins.__dict__[storage_name]

    def qty_setter(ins, value):
        if value > 0:
            ins.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


def main():
    run()


if __name__ == '__main__':
    main()
