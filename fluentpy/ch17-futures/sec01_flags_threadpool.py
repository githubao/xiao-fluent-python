#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多线程下载

@author: BaoQiang
@time: 2017/6/20 16:24
"""

import sys
import time
import os
import requests
from fluentpy.pth import FILE_PATH
from concurrent import futures

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'

BASE_PATH = '{}/flags'.format(FILE_PATH)


def save_flag(img, filename):
    path = os.path.join(BASE_PATH, filename)
    with open(path, 'wb') as fw:
        fw.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    """
    20 flags downloaded in 17.87s
    :return: 
    """
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, '{}.gif'.format(cc.lower()))
    return len(cc_list)


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, '{}.gif'.format(cc.lower()))
    return cc


MAX_WORKERS = 20


def download_many2(cc_list):
    """
    20 flags downloaded in 1.65s
    :param cc_list: 
    :return: 
    """
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))


def download_many3(cc_list):
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


def run(func):
    t1 = time.time()
    count = func(POP20_CC)
    elasped = time.time() - t1
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elasped))


def main():
    # run(download_many)
    # run(download_many2)
    run(download_many3)


if __name__ == '__main__':
    main()
