#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数注解

@author: BaoQiang
@time: 2017/6/13 20:16
"""

from inspect import signature


def clip(text: str, max_len: 'int > 0' = 80) -> str:
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


def anno_run():
    print(clip.__annotations__)

    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)


def main():
    anno_run()


if __name__ == '__main__':
    main()
