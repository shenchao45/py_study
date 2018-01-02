#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :31/12/2017 11:04 AM
# @Author   :shenchao
# @File     :02-file.py
f = open('test.txt', mode='rb')
# f = open('test.txt', mode='w+b')
# f.write('你好，Python！'.encode('utf-8'))
# read = f.read(6)
# print(str(read, encoding='utf-8'))
readline = f.readline()
print(type(readline))
print(str(readline, encoding='utf-8'))
f.close()
