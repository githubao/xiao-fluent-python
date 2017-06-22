#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现一个自己的类工厂函数

@author: BaoQiang
@time: 2017/6/22 14:24
"""


def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass

    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))

        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __repr__=__repr__,
                     __iter__=__iter__,
                     )

    return type(cls_name, (object,), cls_attrs)


def run():
    MyNamedTuple = record_factory('MyNamedTuple', 'name age')
    ins = MyNamedTuple('xiao', 18)
    print(ins)


def main():
    run()


if __name__ == '__main__':
    main()
