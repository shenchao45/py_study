#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :01/01/2018 6:45 PM
# @Author   :shenchao
# @File     :08-module.py
import test11

add = test11.add(1, 2)
print(add)
print(test11.add)


class S:
    pass


print(S)
print(S())
print(hasattr(S, 'abc'))
S.abc = 'hello'
print(hasattr(S, 'abc'))
b = S
print(b)
c = type('MyDog', (), {})
print(c)
print(help(c))
t = type('MyCat', (c,), {'name': 'helo'})
print(help(t))


def myMetaclass(classname, parent, attr):
    newAttr = {}
    for key, value in attr.items():
        if not key.startswith('__'):
            newAttr[key.upper()] = value

    return type(classname, parent, newAttr)


class Foo(object, metaclass=myMetaclass):
    bar = 'bip'


a = Foo()
print(hasattr(a, 'bar'))
print(hasattr(a, 'BAR'))
print(a.BAR)
def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr

c1 = counter(5)
print(c1())
print(c1())

c2 = counter(50)
print(c2())
print(c2())

print(c1())
print(c1())

print(c2())
print(c2())

def t1(fn):
    def test():
        print('hello1')
        print('hello2')
        print('hello3')
        fn()
    return test

@t1
def a():
    print('aaaa')

a()