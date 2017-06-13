#!/usr/bin/env python
# encoding: utf-8

"""
@description: re 字符串匹配

@author: BaoQiang
@time: 2017/6/13 17:09
"""

import re
import os

re_numbers_str = re.compile('\d+')
re_words_str = re.compile('\w+')
re_numbers_bytes = re.compile(b'\d+')
re_words_bytes = re.compile(b'\w+')

text_str = 'Ramanujan saw \u0be7\u0bed\u0be8\u0bef as 1729 = 1³ + 12³ = 9³ + 10³.'
text_bytes = text_str.encode('utf-8')


def re_demo():
    """
    字节模式只能匹配ASCII字符，
    如果str也需要匹配ASCII字符，可以使用re.ASCII标志
    :return: 
    """
    print('Text', repr(text_str), sep='\n ')
    print('Numbers')
    print('str : ', re_numbers_str.findall(text_str))
    print('bytes : ', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print('str : ', re_words_str.findall(text_str))
    print('bytes : ', re_words_bytes.findall(text_bytes))


def file_err():
    """
    文件名包含特殊字符的处理
    :return: 
    """
    print(os.listdir('.'))
    print(os.listdir(b'.'))
    name_bytes = os.listdir(b'.')[1]
    print(name_bytes.decode('ascii', 'surrogateescape'))


def main():
    # re_demo()
    file_err()


if __name__ == '__main__':
    main()
