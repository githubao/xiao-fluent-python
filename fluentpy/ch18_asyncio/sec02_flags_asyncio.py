#!/usr/bin/env python
# encoding: utf-8

"""
@description: 异步爬虫下载

@author: BaoQiang
@time: 2017/6/21 11:22
"""

import sys
import time
import os
import requests
from fluentpy.pth import FILE_PATH
from concurrent import futures

import asyncio
import aiohttp

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

BASE_PATH = '{}/flags'.format(FILE_PATH)


def save_flag(img, filename):
    path = os.path.join(BASE_PATH, filename)
    with open(path, 'wb') as fw:
        fw.write(img)


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield aiohttp.request('GET', url)
    image = yield from resp.read()
    return image


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, '{}.gif'.format(cc.lower()))
    return cc


def run(func):
    t1 = time.time()
    count = func(POP20_CC)
    elasped = time.time() - t1
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elasped))


def main():
    run(download_many)


if __name__ == '__main__':
    main()
