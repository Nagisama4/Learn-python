import gevent
from gevent import monkey
monkey.patch_all() # 需要导入socket之前执行
from socket import *

def handle(c):
	while True:
		data = c.recv(1024)
		if not data:
			break
		print(data.decode())
		c.send(b'OK')


s = socket()
s.bind(('0.0.0.0',8888))
s.listen(10)

while True:
	c, addr = s.accept()
	print("Connect from: ", addr)
	# handle(c)
	gevent.spawn(handle, c)

s.close()

