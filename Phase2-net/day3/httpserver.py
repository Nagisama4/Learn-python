# http server 1.0
# 接收游览器请求，将固定网页发送给游览器

from socket import *

# 处理客户端请求
def handle_request(connfd):
	print("Request from: ", connfd.getpeername())
	request = connfd.recv(4096) # 接收请求
	request_lines = request.splitlines()
	for line in request_lines:
		print(line)

	# 返回固定网页给游览器
	try:
		f = open('index.html')
	except IOError:
		response = "HTTP/1.1 404 Not Found\r\n"
		response += '\r\n'
		response += '404 Not Found'
	else:
		response = "HTTP/1.1 200 OK\r\n"
		response += '\r\n'
		response += f.read()
	finally:
		# 将结果给游览器
		connfd.send(response.encode())
		f.close()

# 创建套接字
def main():
	sockfd = socket()
	sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sockfd.bind(('0.0.0.0', 8000))
	sockfd.listen(3)
	print("Listen the port 8000... ")

	while True:
		connfd, addr = sockfd.accept()
		handle_request(connfd) #具体处理请求
		connfd.close()

if __name__ == "__main__":
	main()

