#　tcp_server.py

import socket 

#　TCP创建套接字
sockfd = socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

#　绑定地址
sockfd.bind(('127.0.0.1',8080))

#　设置监听
sockfd.listen(3)

#　等待客户端连接
print("Waiting for connect ....")
try:
    connfd,addr = sockfd.accept()
except KeyboardInterrupt:
    print("Server exit")
    break
print("Connect from",addr) #　客户端地址

# 消息收发, breakpoint,输入为空直接中断
while True:
    data = input(">>")         
    if not data:
        break 
    data = connfd.recv(1024)   #一次最多接收1024字节
    
    print("Receive message:",data.decode())

n = connfd.send(b"Receive your message")
print("Send %d bytes"%n)

# 关套接字
connfd.close()
sockfd.close()






