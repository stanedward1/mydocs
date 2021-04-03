# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 1:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : myTest.py
# @Software: PyCharm
import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP和端口
server.bind(('127.0.0.1', 8082))
# 监听
server.listen(3)
print('服务器已经启动！')
# 等待连接
clientSocket, clientAddress = server.accept()
print('%s-%s连接成功！' % (str(clientSocket), clientAddress))
while True:
    data = clientSocket.recv(1024)
    print('收到数据：' + data.decode('utf-8'))