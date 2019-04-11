# broadcast_send.py

from socket import *
from time import sleep

# target address
dest = ('176.28.11.34', 9898)

s = socket(AF_INET, SOCK_DGRAM)

# 设置可以发送接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

data = "I want to play a game :)"

while True:
	sleep(1)
	s.sendto(data.encode(),dest)