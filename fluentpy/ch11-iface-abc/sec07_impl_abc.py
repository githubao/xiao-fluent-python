#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自己实现一个抽象基类

@author: BaoQiang
@time: 2017/6/16 18:20
"""

import abc
import random

import doctest

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_classes = list(Tombola._abc_registry)
    for cls in real_subclasses + virtual_classes:
        test(cls, verbose)


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        verbose=verbose,
        optionflags=doctest.PEPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


def run():
    import sys
    main(sys.argv)


class MyExcept():
    """
    BaseException
        SystemExit
        KeyboardInterrupt
        GeneratorExit
        Exception
            StopIteration
            ArithmeticError
                FloatingPointError
                OverflowError
                ZeroDivisionError
            AssertionError
            AttributeError
            BufferError
            EOFError
            ImportError
            LookupError
                IndexError
                KeyError
            MemoryError
    
    """


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):
    """
    注册成为虚拟子类
    Tombola.register(TomboList)
    """

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


def abc_run():
    print(issubclass(TomboList, Tombola))
    t = TomboList()
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)


def main():
    abc_run()


if __name__ == '__main__':
    main()
