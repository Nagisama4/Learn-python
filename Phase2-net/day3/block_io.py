# block_io.py

from socket import *
from time import sleep, ctime

# 创建TCP套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(4)

socfd.setblocking(False)

while True:
	print("waiting for connection")
	try:
		connfd, addr = sockfd.accept()
 