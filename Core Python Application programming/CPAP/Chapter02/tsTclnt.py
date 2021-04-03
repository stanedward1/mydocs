# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 1:51
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : tsTclnt.py
# @Software: PyCharm
from socket import *

from past.builtins import raw_input

# !/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 21568
BUFSIZE = 1024*1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  # 创建套接字
tcpCliSock.connect(ADDR)  # 请求建立连接

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()