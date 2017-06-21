#!/usr/bin/env python
# encoding: utf-8

"""
@description:  线程控制指针的旋转

@author: BaoQiang
@time: 2017/6/20 18:55
"""

import threading
import itertools
import time
import sys
import asyncio


class Signal:
    go = True


@asyncio.coroutine
def spin2(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(0.1)
        except asyncio.CancelledError:
            break

    write('{}{}'.format(' ' * len(status), '\x08' * len(status)))

@asyncio.coroutine
def slow_function2():
    yield from asyncio.sleep(3)
    return 42

@asyncio.coroutine
def supervisor2():
    spinner = asyncio.ensure_future(spin2('thinking!'))
    print('spinner object: ', spinner)
    result = yield from slow_function2()
    spinner.cancel()
    return result


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(0.1)
        if not signal.go:
            break

    write('{}{}'.format(' ' * len(status), '\x08' * len(status)))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object: ', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def run():
    result = supervisor()
    print('Answer: ', result)


def run2():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor2())
    loop.close()
    print('Answer: ', result)


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
