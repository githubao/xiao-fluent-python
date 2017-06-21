#!/usr/bin/env python
# encoding: utf-8

"""
@description: build-in func

@author: BaoQiang
@time: 2017/6/13 17:46
"""


def all_any():
    """
    all(): 都为True，返回True，否则返回False
    any(): 只要有True，返回True，否则返回False
    
    单个判断真假的条件是：None,'',0  

    all([]) 计算结果必须为True，否则“与”运算所有结果都为False
    any([]) 计算结果必须为False，否则“或”运算所有结果都为True
        
    all([a,b]) = a & b & all([])
    any([a,b]) = a | b | any([])
    
    :return: 
    """
    print(all([]))
    print(any([]))


def main():
    all_any()


if __name__ == '__main__':
    main()
