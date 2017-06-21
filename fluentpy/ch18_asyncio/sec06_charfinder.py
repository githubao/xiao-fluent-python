#!/usr/bin/env python
# encoding: utf-8

"""
@description:  字符查找

@author: BaoQiang
@time: 2017/6/21 14:45
"""

import sys
import re
import unicodedata
import warnings
import itertools
import pickle
import functools
from collections import namedtuple

from fluentpy.pth import FILE_PATH

RE_WORD = re.compile('\w+')
RE_UNICODE_NAME = re.compile('^[A-Z0-9 -]+$')
RE_CODEPOINT = re.compile('U\+([0-9A-F]{4,6})')

INDEX_NAME = FILE_PATH + 'charfinder_index.pickle'
MINIMUM_SAVE_LEN = 10000
CJK_UNI_PREFIX = 'CJK UNIFED IDEOGRAPH'
CJK_CMP_PREFIX = 'CJK COMPATIBILITY IDEOGRAPH'

sample_chars = ['$', 'A', 'a', '\u20a0', '\u20ac']

CharDescription = namedtuple('CharDescription', 'code_str char name')
QueryResult = namedtuple('QueryResult', 'count items')


def tokenize(text):
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def query_type(text):
    text_upper = text.upper()
    if 'U+' in text_upper:
        return 'CODEPOINT'
    else:
        return 'CHARACTERS'


class UnicodeNameIndex:
    def __init__(self, chars=None):
        self.load(chars)

    def load(self, chars=None):
        self.index = None
        if chars is None:
            try:
                with open(INDEX_NAME, 'rb') as fp:
                    self.index = pickle.load(fp)
            except OSError:
                pass
        if self.index is None:
            self.build_index(chars)
        if len(self.index) > MINIMUM_SAVE_LEN:
            try:
                self.save()
            except OSError as exc:
                warnings.warn('Could not save {!r}: {}'.format(INDEX_NAME, exc))

    def save(self):
        with open(INDEX_NAME, 'wb') as fp:
            pickle.dump(self.index, fp)

    def build_index(self, chars=None):
        if chars is None:
            chars = (chr(i) for i in range(32, sys.maxunicode))
        index = {}
        for char in chars:
            try:
                name = unicodedata.name(char)
            except ValueError:
                continue
            if name.startswith(CJK_UNI_PREFIX):
                name = CJK_UNI_PREFIX
            elif name.startswith(CJK_CMP_PREFIX):
                name = CJK_CMP_PREFIX

            for word in tokenize(name):
                index.setdefault(word, set()).add(char)

        self.index = index

    def word_rank(self, top=None):
        res = [(len(self.index[key]), key) for key in self.index]
        res.sort(key=lambda item: (-item[0], item[1]))
        if top is not None:
            res = res[:top]
        return res

    def word_report(self, top=None):
        for postings, key in self.word_rank(top):
            print('{:5} {}'.format(postings, key))

    def find_chars(self, query, start=0, stop=None):
        stop = sys.maxsize if stop is None else stop
        results_sets = []
        for word in tokenize(query):
            chars = self.index.get(word)
            if chars is None:
                results_sets = []
                break
            else:
                results_sets.append(chars)

        if not results_sets:
            return QueryResult(0, ())

        result = functools.reduce(set.intersection, results_sets)
        result = sorted(result)
        result_iter = itertools.islice(result, start, stop)
        return QueryResult(len(result), (char for char in result_iter))

    def describe(self, char):
        code_str = 'U+{:04x}'.format(ord(char))
        name = unicodedata.name(char)
        return CharDescription(code_str, char, name.lower())

    def find_descriptions(self, query, start=0, stop=None):
        for char in self.find_chars(query, start, stop).items:
            yield self.describe(char)

    def get_descriptions(self, chars):
        for char in chars:
            yield self.describe(char)

    def describe_str(self, char):
        return '{:7}\t{}\t{}'.format(*self.describe(char))

    def find_description_str(self, query, start=0, stop=None):
        for char in self.find_chars(query, start, stop).items:
            yield self.describe_str(char)

    @staticmethod
    def status(query, counter):
        if counter == 0:
            msg = 'No match'
        elif counter == 1:
            msg = '1 match'
        else:
            msg = '{} matches'.format(counter)
        return '{} for {!r}'.format(msg, query)


def run(*args):
    index = UnicodeNameIndex()
    query = ' '.join(args)
    n = 0
    for n, line in enumerate(index.find_description_str(query), 1):
        print(line)
    print('({})'.format(index.status(query, n)))


def main():
    run(('cat'))


if __name__ == '__main__':
    main()
