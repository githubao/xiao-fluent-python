#!/usr/bin/env python
# encoding: utf-8

"""
@description: 迭代器模式

@author: BaoQiang
@time: 2017/6/19 14:03
"""

import re
import reprlib
import itertools

RE_WORD = re.compile('\w+')



class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


def sentence_lazyiter():
    sen = Sentence('i am good')
    for item in sen:
        print(item)


def while_iter():
    s = 'abc'
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration as e:
            del it
            break


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


def main():
    # while_iter()
    # sentence_lazyiter()
    # print(list(aritprog_gen(0, 1, 3)))
    itertools_run()


if __name__ == '__main__':
    main()
