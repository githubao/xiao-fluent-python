#!/usr/bin/env python
# encoding: utf-8

"""
@description: 并发中的逻辑处理

@author: BaoQiang
@time: 2017/6/20 17:03
"""

import time
from tqdm import tqdm


def process_percent():
    for i in tqdm(range(100)):
        time.sleep(0.01)


def main():
    process_percent()


if __name__ == '__main__':
    main()
