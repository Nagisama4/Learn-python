# recv_file.py

from socket import *

s = socket()
s.bind(('127.0.0.1', 8000))
s.listen(5)

c, addr = s.accept()
print("Connect from ", addr)

f = open('#new file#', 'wb')

while True:
	data = c.recv(1024)
	if not data:
		break
	f.write(data)

f.close()
c.close()
s.close()