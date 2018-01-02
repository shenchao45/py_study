#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :02/01/2018 9:38 AM
# @Author   :shenchao
# @File     :09-gc.py
import sys
import gc
import hashlib

# gc.set_debug(gc.DEBUG_LEAK)

a = 'HelloWorld'
b = a
print(sys.getrefcount(a))
print(sys.getrefcount(a))
del (b)
print(sys.getrefcount(a))
del (a)
print(sys.getrefcount("HelloWorld"))
gc.collect()
print(sys.getrefcount("HelloWorld"))


class Person(object):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


a = Person()
a.name = 12
print(a.name)
a = hashlib.md5()
a.update('123456'.encode())
print(a.hexdigest())