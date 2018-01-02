#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :02/01/2018 10:29 AM
# @Author   :shenchao
# @File     :10-re.py
import re
import requests

result = re.match('shenchao', 'shenchao adsf shenchao')
group = result.group()
print(group)
ret = re.match(".", "a")
ret.group()
print(ret)
ret = re.match(".", "b")
ret.group()
print(ret)
ret = re.match(".", "M")
ret.group()
print(ret)
mm = r'c:\\a\\b\\c'
print(mm)
s = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
a = re.match(r'.+?="(.+?)"', s).group(1)
print(a)
s = '''
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
a = re.findall('http://.+?/',s)
print(a)
