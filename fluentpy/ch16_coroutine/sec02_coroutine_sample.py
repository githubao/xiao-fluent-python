#!/usr/bin/env python
# encoding: utf-8

"""
@description: 一个简单的协程的例子

@author: BaoQiang
@time: 2017/6/19 16:27
"""


class DemoException(Exception):
    pass


def demo_exc_handing():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continueing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
            # raise RuntimeError('this line should never run.')


def coroutine_except():
    coro = demo_exc_handing()
    next(coro)
    coro.send(111)
    coro.send(22)
    coro.throw(DemoException)
    coro.close()


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


def coroutine_run():
    coro = simple_coroutine()
    next(coro)
    coro.send(42)
    # next(coro)


def main():
    # coroutine_run()
    coroutine_except()


if __name__ == '__main__':
    main()
