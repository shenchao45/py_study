#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :01/01/2018 3:17 PM
# @Author   :shenchao
# @File     :07-exception.py
try:
    print('--------test-----1-----')
    print(a)
    open('123.txt', 'r')
    print('--------test-----2-----')
except Exception as e:
    print('出错了%s' % e)
else:
    print('没有捕获到异常')

for x in range(10):
    print(x, end=' ')
else:
    print('没有了')
