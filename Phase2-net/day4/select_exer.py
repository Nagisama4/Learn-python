from select import select
from socket import *
import sys
from time import ctime

# log file
f = open('log.txt', 'a')

s = socket()
s.bind(('',8888))
s.listen(3)

rlist = [s, sys.stdin]
wlist = []
xlist = []

while True:
	# 监控IO
	rs, ws, xs = select(rlist, wlist, xlist)
	for r in rs:
		# s就绪说明有客户端连接
		if r is s:
			c, addr = r.accept()
			print("Connect from ", addr)
			# 将客户端套接字加入关注列表
			rlist.append(c)
		elif r is sys.stdin:
			name = 'Server'
			time = ctime()
			msg  = r.readline()
			f.write('%s  %s  %s\n'%(name, time, msg))
			f.flush()
		else:
			addr = r.getpeername()
			time = ctime()
			msg  = r.recv(1024).decode()
			f.write('%s  %s  %s\n'%(addr, time, msg))
			f.flush()
f.close()
s.close()