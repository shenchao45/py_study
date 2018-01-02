#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
# @Time     :02/01/2018 11:15 AM
# @Author   :shenchao
# @File     :11-requests.py
import requests


# content = requests.get('http://www.baidu.com')
# print(str(content.content, encoding='utf-8'))


def get():
    kw = {'wd': '长城'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)

    # 查看响应内容，response.content返回的字节流数据
    print(response.content)

    # 查看完整url地址
    print(response.url)

    # 查看响应头部字符编码
    print(response.encoding)

    # 查看响应码
    print(response.status_code)


def post():
    formData = {"i": "你好", "from": "AUTO", "to": "AUTO", "smartresult": "dict", "client": "fanyideskweb",
                "salt": "1514863333813", "sign": "45c7d208f113c5087395661814bb2d23", "doctype": "json",
                "version": "2.1", "keyfrom": "fanyi.web", "action": "FY_BY_REALTIME", "typoResult": "false"}

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Referer": "http://fanyi.youdao.com/"
    }

    response = requests.post(url, data=formData, headers=headers)
    print(response.text)

    # 如果是json文件可以直接显示
    print(response.json())


def proxy_get():
    kw = {'wd': 'ip'}
    # 根据协议类型，选择不同的代理
    proxies = {
        "http": "http://118.193.107.153:80",
        "https": "https://101.200.143.168:80",
    }

    response = requests.get("http://www.baidu.com/s", params=kw, proxies=proxies)
    print(str(response.content, encoding='utf-8'))


def auth_get():
    auth = ('test', '123456')
    response = requests.get('http://192.168.199.107', auth=auth)
    print(response.text)


def cookie_get():
    response = requests.get("http://www.baidu.com/")

    # 7. 返回CookieJar对象:
    cookiejar = response.cookies

    # 8. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print(cookiejar)
    print(cookiedict)


def session_get():
    # 1. 创建session对象，可以保存Cookie值
    ssion = requests.session()

    # 2. 处理 headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # 3. 需要登录的用户名和密码
    data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}

    # 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
    ssion.post("http://www.renren.com/PLogin.do", data=data)

    # 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = ssion.get("http://www.renren.com/410043129/profile")

    # 6. 打印响应内容
    print(response.text)


def ssl_get():
    response = requests.get("https://www.12306.cn/mormhweb/", verify=False)
    print(str(response.content, encoding='utf-8'))


if __name__ == '__main__':
    ssl_get()
