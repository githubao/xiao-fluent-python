#!/usr/bin/env python
# encoding: utf-8

"""
@description: with context

@author: BaoQiang
@time: 2017/6/19 15:41
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    print('enter')
    try:
        yield 'hello'
    except Exception as e:
        print('err occur')
    finally:
        print('exit')


with looking_glass() as ins:
    print(ins)


def else_run():
    """
    如果 while try for 等语句正常结束，那么就执行后面紧跟着的else语句
    
    如果异常终止(break except)，就不执行else
    
    :return: 
    """


class A:
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        
        :param exc_type: 
        :param exc_val: 
        :param exc_tb: 
        :return: 
        """


def main():
    pass


if __name__ == '__main__':
    main()
