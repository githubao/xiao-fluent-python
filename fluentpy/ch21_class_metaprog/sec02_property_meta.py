#!/usr/bin/env python
# encoding: utf-8

"""
@description: 属性 装饰器

@author: BaoQiang
@time: 2017/6/22 14:33
"""

from fluentpy.ch20_descriptor.sec20_diy_property import Quantity3, Validated, NoBlank
import collections


def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls


class EntityMeta(type):
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls.field_names = []
        # for key, attr in cls.__dict__.items():
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)

                cls.field_names.append(key)

    @classmethod
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()


class Entity2(metaclass=EntityMeta):
    @classmethod
    def field_names(cls):
        for name in cls._field_names:
            yield name


# @entity
class LineItem(Entity2):
    weight = Quantity3()
    description = NoBlank()
    price = Quantity3()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def run():
    ins = LineItem('he', 70, 30)
    for item in ins.field_names:
        print(item)
    print(dir(ins))


def main():
    run()


if __name__ == '__main__':
    main()
