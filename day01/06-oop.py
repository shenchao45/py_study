#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :01/01/2018 2:09 PM
# @Author   :shenchao
# @File     :06-oop.py
class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'name=%s,age=%d' % (self.__name, self.__age)

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age


s = Student('wzh', 18)
s.name = 'sc'
s.setName('sc')
print(s)


class Cat(object):
    def sayHello(self):
        print("halou-----1")


class Bosi(Cat):
    def sayHello(self):
        print("halou-----2")


bosi = Bosi()
bosi.sayHello()
