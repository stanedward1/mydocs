# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 1:33
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : tsTserv.py
# @Software: PyCharm
from socket import *
from time import ctime

# 给出地址，and，缓存区大小设置为1kb
HOST = '127.0.0.1'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 绑定后，设置传入连接请求的最大数
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print ('waiting for connection')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connection from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(("[%s] %s" % (ctime(), data)).encode())
    tcpCliSock.close()
tcpSerSock.close()