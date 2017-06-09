#!/usr/bin/env python
# encoding: utf-8

"""
@description: 所有的magic method

@author: BaoQiang
@time: 2017/6/9 17:55
"""


class MagicMethod:
    def str_method(self):
        """
        str
        """

        def __repr__():
            pass

        def __str__():
            pass

        def __format__():
            pass

        def __bytes__():
            pass

    def int_method(self):
        """
        int
        """

        def __abs__():
            pass

        def __bool__():
            pass

        def __complex__():
            pass

        def __int__():
            pass

        def __float__():
            pass

        def __hash__():
            pass

        def __index__():
            pass

    def collection_method(self):
        """
        collection
        """

        def __len__():
            pass

        def __getitem__():
            pass

        def __setitem__():
            pass

        def __delitem__():
            pass

        def __contains__():
            pass

    def iter_method(self):
        """
        iter
        """

        def __iter__():
            pass

        def __reversed__():
            pass

        def __next__():
            pass

    def func_method(self):
        """
        func
        """

        def __call__():
            pass

    def with_method(self):
        """
        with
        """

        def __enter__():
            pass

        def __exit__():
            pass

    def instance_method(self):
        """
        instance
        """

        def __new__():
            pass

        def __init__():
            pass

        def __del__():
            pass

    def attr_method(self):
        """
        attr
        """

        def __getattr__():
            pass

        def __setattr__():
            pass

        def __delattr__():
            pass

        def __dir__():
            pass

        def __getattribute__():
            pass

    def property_method(self):
        """
        property
        """

        def __get__():
            pass

        def __set__():
            pass

        def __delete__():
            pass

    def class_method(self):
        """
        class
        """

        def __prepare__():
            pass

        def __instancecheck__():
            pass

        def __subclasscheck__():
            pass

    def oneop_method(self):
        """
        oneop
        """

        def __neg__():
            pass

        def __pos__():
            pass

        def __abs__():
            pass

    def cmpop_method(self):
        """
        cmpop
        """

        def __lt__():
            pass

        def __le__():
            pass

        def __eq__():
            pass

        def __ne__():
            pass

        def __gt__():
            pass

        def __ge__():
            pass

    def arithop_method(self):
        """
        arithop
        """

        def __add__():
            pass

        def __sub__():
            pass

        def __mul__():
            pass

        def __truediv__():
            pass

        def __floordiv__():
            pass

        def __mod__():
            pass

        def __divmod__():
            pass

        def __pow__():
            pass

        def __round__():
            pass

    def rarithop_method(self):
        """
        rarithop
        """

        def __radd__():
            pass

        def __rsub__():
            pass

        def __rmul__():
            pass

        def __rtruediv__():
            pass

        def __rfloordiv__():
            pass

        def __rdivmod__():
            pass

        def __rpow__():
            pass

    def iarithop_method(self):
        """
        iarithop
        """

        def __iadd__():
            pass

        def __isub__():
            pass

        def __imul__():
            pass

        def __itruediv__():
            pass

        def __ifloordiv__():
            pass

        def __imod__():
            pass

        def __ipow__():
            pass

    def bitop_method(self):
        """
        bitop
        """

        def __invert__():
            pass

        def __lshift__():
            pass

        def __rshift__():
            pass

        def __add__():
            pass

        def __or__():
            pass

        def __xor__():
            pass

    def rbitop_method(self):
        """
        rbitop
        """
        def __rlshift__():
            pass

        def __rrshift__():
            pass

        def __radd__():
            pass

        def __ror__():
            pass

        def __rxor__():
            pass

    def ibitop_method(self):
        """
        ibitop
        """
        def __ilshift__():
            pass

        def __irshift__():
            pass

        def __iadd__():
            pass

        def __ior__():
            pass

        def __ixor__():
            pass

def main():
    print('do sth')


if __name__ == '__main__':
    main()
