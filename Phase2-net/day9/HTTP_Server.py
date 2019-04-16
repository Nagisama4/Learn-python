"""
HTTP Server 2.0
"""
from socket import *
from threading import Thread
import sys


# 封装HTTP类作为一个完整的服务功能
class HTTPServer(object):
	def __init__(self, server_addr, statis_dir):
		self.server_address = server_addr
		self.statis_dir = static_dir
		self.create_socket()
		self.bind()

	def create_socket(self):
		self.sockfd = socket()
		self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	def bind(self):
		self.sockfd.bind(self.server_address)
		self.ip = self.server_address[0]
		self.port = self.server_address[1]

	def serve_forever(self):
		self.sockfd.listen(5)
		print("Listen the port %d"%self.port)
		while True:
			try:
				connfd, addr = self.sockfd.accept()
			except KeyboardInterrupt:
				self.sockfd.close()
				sys.exit()
			except Exception as e:
				print(e)
				continue
			# 创建新的线程处理请求
			th = Thread(target = self.handle, args = (connfd, ))
			th.setDaemon(True)
			th.start()

	# 处理游览器请求
	def handle(self, connfd):
		# 接收HTTP请求
		request = connfd.recv(4096)

		# 防止异常断开
		if not request:
			return
		# 请求解析
		requestHeaders = request.splitlines()
		print(connfd.getpeername(), ':', requestHeaders[0])
		# 获取请求内容
		getRequest = str(requestHeaders[0]).split(' ')[1]

		if getRequest == '/' or getRequest[-5:] == '.html':
			self.get_html(connfd, getRequest)
		else:
			self.get_data(connfd, getRequest)

	def get_html(self, connfd, getRequest):
		if getRequest == '/':
			filename = self.static_dir + '/index.html'
		else:
			filename = self.static_dir + getRequest
		try:
			f = open(filename)
		except IOError:
			responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
			responseHeaders += '\r\n'
			responseBody = "404 Not Found"
		else:
			responseHeaders = 'HTTP/1.1 200 OK\r\n'
			responseHeaders += '\r\n'
			responseBody = f.read()
		finally:
			reponse = responseHeaders + responseBody
			connfd.send(reponse.encode())

	def get_data(self, connfd, getRequest):
		data = """HTTP/1.1 200 OK

		<p>Waiting httpserver 3.0</p>
		"""
		connfd.send(data.encode())

if __name__ == '__main__':
	server_addr = ('0.0.0.0', 8000)
	static_dir  = "./statis" # 网页存放位置
	# 生成服务器对象
	httpd = HTTPServer(server_addr, static_dir)
	# 启动服务
	httpd.serve_forever()