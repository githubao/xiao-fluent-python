#!/usr/bin/env python
# encoding: utf-8

"""
@description: 命令模式

@author: BaoQiang
@time: 2017/6/13 21:19
"""


class MacroCommand:
    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for cmd in self.commands:
            cmd()


def main():
    print('do sth')


if __name__ == '__main__':
    main()
