#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现抽象基类

@author: BaoQiang
@time: 2017/6/16 18:05
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class MyInt():
    """
    数字类抽象层次
    Number
    Complex
    Real
    Rational
    Integral
    
    :return: 
    """


class FrenchDeck(collections.MutableSequence):
    """
    collections.abc 里面的抽象基类列表
    
    Iterable
    Container
    Sized
    Callable
    Hashable
    
    Iterator
    Sequence
    Mapping
    Set
    MappingView
    
    MutableSequence
    MutableMapping
    MutableSet
    ItemsView
    KeysView
    ValuesView
    
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, index, value):
        self._cards.insert(index, value)


def main():
    """
    FrenchDeck, MutableSequence, Sequence, Sized, Iterable, Container, object
    :return: 
    """
    print(', '.join(c.__name__ for c in FrenchDeck.__mro__))


if __name__ == '__main__':
    main()
