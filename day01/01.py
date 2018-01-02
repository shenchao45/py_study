#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :30/12/2017 2:50 PM
# @Author   :shenchao
# @File     :01.py

import keyword

print('hello world')
print('这里是中文')
num1 = 100
num2 = 87
result = num1 + num2
print(result)
print(dir(keyword))
# 输出格式化
age = 10
print("我今年%d岁" % age)
age += 1
print("我今年%d岁" % age)
name = "小王"
print("我的姓名是%s，年龄是%d" % (name, age))
print("1234567890\n00000000")
# 输入
# password = input('请输入密码：')
password = '1'
print('您刚刚输入的密码是：', password, "dasf")
print(type(password))
print("sdfa" + "dsafsa")
a, b = 1, 2
print(a)
print(b)
print(10 ** 10)
print(int(password, 9))
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d' % (j, i, j * i), end=' ')
        j += 1
    print()
    i += 1
name = 'shenchao'
name = 'dsafdsaf'
for x in name:
    print(x)
else:
    print('没有数据')

print('---------------------------------')
i = 9
for x in range(i):
    if x < i // 2:
        k = x + 1
    else:
        k = 9 - x
    for x in range(k):
        print("* ", end='')
    print()
print('---------------------------------')
s = 'aStr'
print(s[::-1])
print('---------------------------------')
s = 'hello world ni hao shijie'
b = {}
for x in s:
    b[x] = b.get(x, 0) + 1
print("summary：", b)


def printInfo():
    # 这里是函数文档说明
    "用来打印logo的"
    print('-' * 50)
    print('人生苦短，我用Python'.center(50))
    print('-' * 50)

printInfo()
print(help(printInfo))
