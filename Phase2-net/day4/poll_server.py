# poll_server.py

from select import *
from socket import *

# 创建套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8000))
s.listen(5)

# 创建poll对象
p = poll()

# 建立地图(字典)
fdmap = {s.fileno():s}

# 关注IO
p.register(s, POLLIN|POLLERR)

#循环监控
while True:
	events = p.poll()
	# 遍历events, 处理IO
	for fd, event in events:
		if fd == s.fileno():
			c, addr = fdmap[fd].accept()
			print("Connect from ", addr)
			# 添加新的关注IO
			p.register(c,POLLIN|POLLUP)
			fdmap[c.fileno()] = c
		elif event & POLLUP:
			print("Exit client")
			p.unregister(fd)
			fdmap[fd].close()
			del fdmap[fd]
		elif event & POLLIN:
			data = fdmap[fd].recv(1024)
			print(data.decode())
			fdmap[fd].send(b'OJBK')
