#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串的统一比较形式

@author: BaoQiang
@time: 2017/6/13 10:26
"""

from unicodedata import normalize
import unicodedata
import string
import pyuca
import re


def unicode_run():
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(normalize('NFC', s1) == normalize('NFC', s2))
    print(normalize('NFD', s1) == normalize('NFD', s2))


def fold_equal(str1, str2):
    """
    忽略大小写的字符比较：“大小写折叠”
    :param str1: 
    :param str2: 
    :return: 
    """
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


def shave_marks_latin(txt):
    """
    把变音符号去掉，表示成规范化的形式
    :param txt: 
    :return: 
    """
    norm_txt = normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)


def unicode_cmp():
    coll = pyuca.Collator()
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    sorted_fruits = sorted(fruits, key=coll.sort_key)
    print(sorted_fruits)


def unicode_info():
    re_digit = re.compile('\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
        print('U+{:4x}'.format(ord(char)),
              char.center(6),
              're_dig' if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(unicodedata.numeric(char), "5.2f"),
              unicodedata.name(char),
              sep='\t'
              )


def main():
    # unicode_run()
    # unicode_cmp()
    unicode_info()


if __name__ == '__main__':
    main()
