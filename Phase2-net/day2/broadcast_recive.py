# broadcast_recieve.py

from socket import *

# 创建套接字
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

# 选择接收地址
s.bind(('0.0.0.0',9898))

while True:
	msg, addr = s.recvfrom(1024)
	print(msg.decode())