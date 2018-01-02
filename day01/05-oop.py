#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :31/12/2017 11:56 AM
# @Author   :shenchao
# @File     :05-oop.py
stu_a = {
    'name': 'A',
    'age': 21,
    'gender': 1,
    'hometown': '江苏'
}
stu_b = {
    'name': 'B',
    'age': 21,
    'gender': 1,
    'hometown': '江苏'
}
stu_c = {
    'name': 'C',
    'age': 21,
    'gender': 1,
    'hometown': '江苏'
}
print(type(stu_a))


def stu_intro(stu):
    """自我介绍"""
    for key, value in stu.items():
        print('key=%s,value=%s' % (key, value))


stu_intro(stu_a)
stu_intro(stu_b)
stu_intro(stu_c)


class Car:
    def __init__(self, wheelNum, color):
        self.wheelNum = wheelNum
        self.color = color

    def getCarInfo(self):
        print('车轮子个数：%d，颜色是%s' % (self.wheelNum, self.color))

    def move(self):
        print('车正在移动。。。。')

    def __str__(self):
        return '%s,%s' % (self.wheelNum, self.color)


BMW = Car(4, '白色')
BMW.color = '黑色'
BMW.wheelNum = 4  # 轮子的数量
BMW.move()
BMW.getCarInfo()
print(BMW)
