#!/usr/bin/env python
# encoding: utf-8

"""
@description: dict

@author: BaoQiang
@time: 2017/6/12 14:41
"""

import builtins
from collections import ChainMap
from collections import UserDict
from types import MappingProxyType

def dict_demo():
    a = 1
    b = 2
    dic = dict.fromkeys((1, 2), 'default')
    print(dic)

    dic.clear()
    dic.setdefault(a, []).append(b)
    print(dic)


def dict_demo2():
    # pylookup = ChainMap(locals(), globals(), vars(builtins))
    pylookup = ChainMap(locals(), globals())
    for k, v in pylookup.items():
        print(k, v)


class StrKeyDict(UserDict):
    """
    由于dict的一些特殊实现，使用UserDict作为字典类型继承的基类，会更优雅
    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


def dict_demo3():
    dic = {1:'a'}
    dic_proxy = MappingProxyType(dic)
    print(dic_proxy)
    # fail
    # dic[1] = 'b'
    # pass
    dic[2] = 'b'
    print(dic_proxy)

def main():
    # dict_demo()
    # dict_demo2()
    dict_demo3()


if __name__ == '__main__':
    main()
