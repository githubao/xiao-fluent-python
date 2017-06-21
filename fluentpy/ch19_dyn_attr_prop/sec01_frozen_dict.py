#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现点号运算符

@author: BaoQiang
@time: 2017/6/21 17:29
"""

import json
from collections import abc
import keyword

from fluentpy.pth import FILE_PATH
import shelve
import inspect

db_name = '{}/shelve/coonn'.format(FILE_PATH)
file_path = '{}/shelve/coonn.json'.format(FILE_PATH)
CONFERENCE = 'conference.115'


class MissingDatabaseError(RuntimeError):
    pass


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class DBRecord(Record):
    __db = None

    @staticmethod
    def set_db(db):
        DBRecord.__db = db

    @staticmethod
    def get_db():
        return DBRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = 'database not set, call "{}.set_db(my_db)"'
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DBRecord):
    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)

        # 使用类的“fetch”方法，而不是可能的属性“fetch”
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()


def load():
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_db2(db):
    raw_data = load()
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]

        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DBRecord)
        if inspect.isclass(cls) and issubclass(cls, DBRecord):
            factory = cls
        else:
            factory = DBRecord

        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)


def load_db(db):
    raw_data = load()
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON(self.__data[item])

    @classmethod
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg


def run():
    with shelve.open(db_name) as db:
        if CONFERENCE not in db:
            load_db(db)

        print(db['speaker.157509'])


def run2():
    fj = FrozenJSON(json.loads(data))
    print(fj.Schedule.conferences[0].serial)


data = """

"""


def main():
    run()


if __name__ == '__main__':
    main()
