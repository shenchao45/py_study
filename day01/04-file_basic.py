#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :31/12/2017 11:30 AM
# @Author   :shenchao
# @File     :04-file_basic.py
import os

f = open('test.txt', 'rb')
content = f.read(3)
print(str(content, encoding='utf-8'))
# 查找当前文件位置
position = f.tell()
print(position)
f.seek(6, 0)
content = f.read(3)
print(str(content, encoding='utf-8'))
f.seek(-6, 2)
print(f.tell())
content = f.read()
print(str(content, encoding='utf-8'))
# os.rename('test[复件].txt', '沈超.txt')
# os.remove('沈超.txt')
f.close()
# os.mkdir('沈超')
path = os.getcwd()
print(path)
os.chdir('../../')
path = os.getcwd()
print(path)
os.chdir('py_study/day01')
# os.rmdir('沈超')
os.chdir('../')
listdir = os.listdir('./')
print(listdir)
