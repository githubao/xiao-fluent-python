#!/usr/bin/env python
# encoding: utf-8

"""
@description: 常见的编码

@author: BaoQiang
@time: 2017/6/12 16:34
"""

import chardet
import sys
import locale
from fluentpy.pth import FILE_PATH

myfile = open('{}/dummy.txt'.format(FILE_PATH), 'w')


def codec_demo():
    """
    cp = code page
    latin1(iso8859_1)
    cp1252
    gb2312
    gbk(cp936)
    utf-8
    utf-16le
    大端，小端：
    小端，低位的数据，在内存真实地址的低位
    大端，低位的数据，在内存真实地址的高位
    
    小端：强制转化数据
    大端：方便判断符号位正负
    
    :return: 
    """
    pass


def codecerr_demo():
    """
    b'bi jng'
    b'b?i j?ng'
    b'b&#283;i j&#299;ng'
    :return: 
    """
    city = 'běi jīng'
    # print(city.encode('cp437', errors='strict'))
    print(city.encode('cp437', errors='ignore'))
    print(city.encode('cp437', errors='replace'))
    print(city.encode('cp437', errors='xmlcharrefreplace'))


def chardet_demo():
    """
    {'encoding': 'utf-8', 'confidence': 0.99}
    {'encoding': 'GB2312', 'confidence': 0.99}
    :return: 
    """
    s = '中华人民共和国'
    print(chardet.detect(s.encode('utf-8')))
    print(chardet.detect(s.encode('gbk')))

    """
    b'\xff\xfe'。这是 BOM，即字节序标记（byte-order mark），指明编码时使
    用 Intel CPU 的小字节序。
    在小字节序设备中，各个码位的最低有效字节在前面：字母 'E' 的码位是 U+0045（十进
    b'\xff\xfe-NNS\xbaN\x11lqQ\x8cT\xfdV'
    """
    print(s.encode('utf-16'))


def default_code():
    """
 locale.getpreferredencoding() -> cp936
                  type(myfile) -> <class '_io.TextIOWrapper'>
               myfile.encoding -> cp936
           sys.stdout.isatty() -> False
           sys.stdout.encoding -> UTF-8
            sys.stdin.isatty() -> False
            sys.stdin.encoding -> UTF-8
           sys.stderr.isatty() -> False
           sys.stderr.encoding -> UTF-8
      sys.getdefaultencoding() -> utf-8
   sys.getfilesystemencoding() -> mbcs

    :return: 
    """

    func_lst = [
        'locale.getpreferredencoding()',
        'type(myfile)',
        'myfile.encoding',
        'sys.stdout.isatty()',
        'sys.stdout.encoding',
        'sys.stdin.isatty()',
        'sys.stdin.encoding',
        'sys.stderr.isatty()',
        'sys.stderr.encoding',
        'sys.getdefaultencoding()',
        'sys.getfilesystemencoding()'
    ]

    for func in func_lst:
        print('{:>30} -> {}'.format(func,eval(func)))


def main():
    # codecerr_demo()
    # chardet_demo()
    default_code()


if __name__ == '__main__':
    main()
