#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :31/12/2017 11:16 AM
# @Author   :shenchao
# @File     :03-copy.py
oldFileName = input('请输入要拷贝的文件的名字：')
oldFile = open(oldFileName, 'rb')
if oldFile:
    fileFlagNum = oldFileName.rfind('.')
    if fileFlagNum > 0:
        fileFlag = oldFileName[fileFlagNum:]
    # 组织新的文件名字
    newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
    # 创建新文件
    newFile = open(newFileName, 'w+b')
    content = oldFile.read(1024)
    while content:
        newFile.write(content)
        content = oldFile.read(1024)
    newFile.close()
    oldFile.close()
