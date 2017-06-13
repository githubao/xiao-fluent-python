#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数

@author: BaoQiang
@time: 2017/6/13 18:02
"""

import bobo
from inspect import signature


class A:
    pass


ins = A()


def func():
    pass


def func_demo():
    """
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
    :return: 
    """
    print(dir(func))
    print(sorted(set(dir(func)) - set(dir(ins))))


def tag(name, *content, classname=None, **attrs):
    if classname is not None:
        attrs['class'] = classname
    if attrs:
        attr_str = ''.join(' {}="{}"'.format(attr, value) for attr, value in attrs.items())
    else:
        attr_str = ''

    if content:
        return '\n'.join('<{}{}>{}<{}>'.format(name, attr_str, c, name) for c in content)
    else:
        return '<{}{} />'.format(name, attr_str)


@bobo.query('/')
def hello(person):
    """
    http://localhost:8080/ :Missing form variable person
    http://localhost:8080/?person=xiaobao : Hello xiaobao!
    :param person: 
    :return: 
    """
    return 'Hello {}!'.format(person)


def clip(text, max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


def inspect_demo():
    """
    POSITIONAL_OR_KEYWORD: 关键字参数
    VAR_POSITIONAL: 定位参数元组
    VAR_KEYWORD: 关键字参数字典
    KEYWORD_ONLY： 仅限关键字参数
    POSITONAL_ONLY： 仅限定位参数
    :return: 
    """

    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)

    sig = signature(clip)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ': ', name, '=', param.default)

    my_tag = {'name': 'img'}
    sig = signature(tag)
    bound_args = sig.bind(**my_tag)
    print(bound_args)


def main():
    # func_demo()
    inspect_demo()


if __name__ == '__main__':
    main()
