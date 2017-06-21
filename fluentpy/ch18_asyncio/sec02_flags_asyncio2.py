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

import asyncio
import aiohttp
from collections import namedtuple
from fluentpy.pth import FILE_PATH
from enum import Enum
from aiohttp import ClientSession
import collections

import tqdm


class HTTPStatus(Enum):
    ok = 1,
    not_found = 2,
    error = 3


from aiohttp import web

DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

BASE_PATH = '{}/flags'.format(FILE_PATH)
Result = namedtuple('Result', 'status data')


def save_flag(img, filename):
    path = os.path.join(BASE_PATH, filename)
    with open(path, 'wb') as fw:
        fw.write(img)


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield ClientSession().request('GET', url)
    if resp.status == 200:
        image = yield from resp.read()
        return image
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(
            code=resp.status, message=resp.reason, headers=resp.headers
        )


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


@asyncio.coroutine
def download_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in cc_list]

    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))
    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status

        counter[status] += 1
    return counter


def download_many(cc_list,base_url,verbose,concer_req):
    loop = asyncio.get_event_loop()
    coro = download_coro(cc_list,base_url,verbose,concer_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts

@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            image = yield from get_flag(cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        # save_flag(image, '{}.gif'.format(cc.lower()))
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None,save_flag,image,'{}.gif'.format(cc.lower()))

        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status.cc)


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
