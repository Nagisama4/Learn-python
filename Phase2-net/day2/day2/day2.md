## 前情回顾

>1. *OSI七层模型  TCP/IP模型*
>2. *三次握手和四次挥手*
>3. *tcp和udp的区别*
>4. *网络概念 ： 网络主机，端口，IP地址  域名*
>5. *套接字编程：网络编程技术手段*
>6. *TCP套接字通信*

>* 服务器：`socket()` --> `bind()` --> `listen()` --> `accept()` --> `recv/send` --> `close()`

>* 客户端：`socket()` --> `connect()` --> `send/recv` --> `close()`

************************************************
## 一. tcp套接字数据传输特点

1. tcp连接中当一端退出，另一端如果阻塞在recv，则recv会立即返回一个空字串

2. tcp连接中如果另一端已经不存在，再试图使用send向其发送内容时会出现BrokenPipeError

3. 网络收发缓冲区

	+ 缓冲区有效的协调了消息的收发速度
	+ send，recv实际是向缓冲区发送接收消息，当缓冲区不为空的时候recv就不会阻塞
   
4. 粘包问题

	**原因：** tcp以字节流方式传输数据，没有消息边界，多次发送的内容如果被一次接收就会形成粘包

	**影响：** 如果每次发送的内容是需要独立解析的含义，此时粘包会对消息的解析产生影响

	**处理：** 1. 人为添加消息边 | 2. 控制发送速度

## 二. UDP套接字编程

### 1. 服务端流程

#### (1). 创建套接字

```python
sockfd = socket(AF_INET,SOCK_DGRAM)
```

#### (2). 绑定地址

```python
sockfd.bind(addr)
```

#### (3). 收发消息

```python
data,addr = sockfd.recvfrom(buffersize)
```

>* 功能: 接收UDP消息
>* 参数： 每次最多接收多少字节内容
>* 返回值：`data` 接收到的消息 | `addr` 消息发送方地址

```python
n = sockfd.sendto(data,addr)
```

>* 功能: 发送UDP消息
>* 参数：`data` 发送的内容 | `bytes`格式 | `addr` 目标地址
    
#### (4). 关闭套接字

```python
sockfd.close()
```

### 2. 客户端流程
	   
#### (1). 创建udp套接字
#### (2). 发送接收消息
#### (3). 关闭套接字

### 总结 ： tcp套接字和udp套接字编程区别

>1. **流式套接字式以字节流方式传输数据，数据报套接字以数据报形式传输**
>2. **TCP套接字会有粘包问题，UDP套接字由消息边界不会粘包**
>3. **TCP套接字保证消息的完整性，UDP不保障**
>4. **TCP套接字依赖`listen` `accept`完成连接才能进行数据收发，UDP套接字不需要**
>5. **TCP使用`send` `recv`收发消息，UDP使用`sendto`, `recvfrom`**

## 二. socket模块方法和socket套接字属性

### 1. 部分socket模块方法

>* 获取计算机名： 

```python
socket.gethostname()
```

>* 通过主机名获取ip地址

```python
socket.gethostbyname('www.baidu.com') 
```

>* 通过服务名称获取监听端口

```python
socket.getservbyname('mysql')
```

>* 通过端口获取服务名称

```python
socket.getservbyport(3306)
```

>* 将IP地址转换为字节串

```python
socket.inet_aton('192.168.1.2')
```

>* 将字节串转换为IP

```python
socket.inet_ntoa(b'\xc0\xa8\x01\x02')
```


### 2. 套接字属性

>- `sockfd.family`  地址类型
>- `sockfd.type`  套接字类型
>- `sockfd.getsockname()` 获取套接字绑定地址
>- `sockfd.fileno()` 获取文件描述符
	
	文件描述符：系统中每一个IO操作都会分配一个整数作为编号，该整数即这个IO的文件描述符。
	特点：每个IO的文件描述符不会重复

>- `getpeername()` 获取连接套接字客户端地址
>- `setsockopt(level,option,value)`

	功能：设置套接字选项
	参数：
		level  | 选项类别 | SOL_SOCKET  
		option | 具体选项内容 
		value  | 选项值

## 三. UDP套接字广播

>- 广播定义：一端发送，多端接收

>- 广播地址：每个网段内的最大地址，向该地址发送则网段内所有的主机都能接收。

## 四. TCP套接字之HTTP传输

1. HTTP协议（超文本传输协议）
用途：网页的传输，数据传输
特点: 应用层协议，传输层使用tcp服务；简单，灵活，无状态；请求类型多样，数据格式支持全面
     
2. HTTP请求格式

	  【1】 请求行 ： 具体的请求类别和请求内容
		      
					格式 :    GET        /      HTTP/1.1
                 请求类别  请求内容   协议版本
					
					请求类别：每个请求类别表达不同的请求方式和行为

					  GET  : 获取网络资源
						POST ：提交一定的信息，得到反馈
						HEAD ：只获取网络资源响应头
						PUT  ：更新服务器资源
						DELETE ： 删除服务器资源
						CONNECT
						TRACE ： 测试
						OPTIONS ： 获取服务器性能信息


		【2】 请求头 ： 对请求的进一步描述和解释
				Accept-Encoding: gzip

		【3】 空行
		【4】 请求体: 请求参数或者提交内容

作业：1. 使用tcp套接字完成一个文件的传输，要求从客户端将文件发送给服务端，文件类型能够是文本或者图片等。
      2. 要求能够自己写出tcp和udp的基础代码

