# udp_server.py

from socket import *

# UDP创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)  # (addr, port)
sockfd.bind(server_addr)

# 收发消息
while True:
	data, addr = sockfd.recvfrom(1024)
	print("Receive from %s:%s"%(addr, data.decode()))
	sockfd.sendto(b"Thanks for your msg", addr)

# 关闭套接字
sockfd.close()