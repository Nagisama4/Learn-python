from select import select
from socket import *

f = open('39954.jpg')
s = socket()
s.bind(('127.0.0.1', 9000))
s.listen(4)

print("监控中...")
rs, ws, xs = select([s,f], [], [])
print(rs)
print(ws)
print(xs)