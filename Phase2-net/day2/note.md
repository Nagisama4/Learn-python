# 【服务端流程】

# UDP创建套接字
socketfd = socket(AF_INET)

# 绑定地址
sockfd.bind(addr)

# 收发消息
data, addr = sockfd.recvfrom(buffersize)
# 功能：接收UDP消息
# 参数：每次最多接收多少字节内容
# 返回值：data 接收的消息   addr 消息发送方地址

n = sockfd.sendto(data, addr)
# 功能：发送UDP消息
# 参数：data 发送的内容   bytes 格式   addr 地址

# 关闭套接字
sockfd.close()


# 【客户端流程】

# 创建UDP套接字

# 发送接收消息

# 关闭套接字

#-----------------------------------------------------------------------#

socket.gethostname()
# 获取计算机名

socket.gethostbyname('www.pornhub.com')
# 通过主机名获取ip地址

socket.getservbyname('ssh')
# 通过服务名称获取监听端口

socket.getservbyport(80)
# 通过端口获取服务名称

socket.inet_aton('192.168.1.2')


b'\xc0\xa8\x01\x02'

sockfd.fileno()

sys.std.filein()

getpeername()
# 获取连接套接字客户端地址

setsockopt(level, option, value)
# 设置套接字选项
# 参数： level 选项类别   option 具体选项内容   value 选项值

#-----------------------------------------------------------------------#

# UDP套接字广播
# 广播定义： 一端发送，多端接收
# 广播地址： 每个网段内的最大地址

# TCP套接字，HTTP传输
# 
0