#!/usr/bin/env python
# encoding: utf-8

"""
@description: 结构体

@author: BaoQiang
@time: 2017/6/12 16:24
"""

import struct
from fluentpy.pth import FILE_PATH


def struct_demo():
    """
    b'GIF89a\x90\x01\xe1\x00'
    (b'GIF', b'89a', 400, 225)
    
    fmt = '<3s3sHH'
    小字节序 两个3字节序列 两个16位二进制整数
    用什么样的格式解释内存中的数据
    
    :return: 
    """

    fmt = '<3s3sHH'
    with open('{}/226109.gif'.format(FILE_PATH), 'rb') as fp:
        img = memoryview(fp.read())
    header = img[:10]
    print(bytes(header))
    print(struct.unpack(fmt, header))


def main():
    struct_demo()


if __name__ == '__main__':
    main()
