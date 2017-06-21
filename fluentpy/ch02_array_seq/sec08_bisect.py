#!/usr/bin/env python
# encoding: utf-8

"""
@description: 有序序列插入

@author: BaoQiang
@time: 2017/6/12 11:18
"""

from random import random
from array import array
import bisect

data = [4, 2, 9, 7]


def demo():
    data.sort()

    bisect.insort(data, 3)
    print(data)

    # 返回将要插入的位置，但是不插入
    print(bisect.bisect(data, 8))

    # 如果存在相同的数据，在左边还是右边插入
    print(bisect.bisect_left(data, 4))
    print(bisect.bisect_right(data, 4))


def array_run():
    """
    Type code	C Type	Python Type	Minimum size in bytes	Notes
    'b'	signed char	int	1	 
    'B'	unsigned char	int	1	 
    'u'	Py_UNICODE	Unicode character	2	(1)
    'h'	signed short	int	2	 
    'H'	unsigned short	int	2	 
    'i'	signed int	int	2	 
    'I'	unsigned int	int	2	 
    'l'	signed long	int	4	 
    'L'	unsigned long	int	4	 
    'q'	signed long long	int	8	(2)
    'Q'	unsigned long long	int	8	(2)
    'f'	float	float	4	 
    'd'	double	float	8	 
    :return: 
    """

    floats = array('d', (random() for _ in range(10 * 4)))
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp)
    fp.close()


def main():
    demo()


if __name__ == '__main__':
    main()
