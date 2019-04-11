# sock_attr.py

from socket import *

s = socket()

print(s.family)
print(s.type)

s.bind('0.0.0.0', 8888)
print(s.getsockname())
print(s.fileno)

s.listen(3)
c, addr = s.accept()
print(c.getpeername)

