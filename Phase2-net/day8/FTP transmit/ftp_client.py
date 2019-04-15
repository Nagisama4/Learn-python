from socket import *
import sys
import time

ADDR = ('127.0.0.1', 8888)

class FtpClient(object):
	def __init__(self, sockfd):
		self.sockfd = sockfd

	def do_list(self):
		self.sockfd.send(b'L') # 发送请求
		# wait for response
		data = self.sockfd.recv(128).decode()
		if data == 'OK':
			files = self.sockfd.recv(4096).decode()
			for file in files.split('#'):
				print(file)
		else:
			# 无法完成操作
			print(data)

	def do_quit(self):
		self.sockfd.send(b'Q')
		self.sockfd.close()
		sys.exit('Bye')

	def do_get(self, filename):
		self.sockfd.send(('G ' + filename).encode())
		data = self.sockfd.recv(128).decode()
		if data == 'OK':
			fd = open(filename, 'wb')
			while True:
				data = self.sockfd.recv(1024)
				if data == b'##':
					break
				fd.write(data)
			fd.close()
		else:
			print(data)

	def do_put(self, filename):
		self.sockfd.send(('P ' + filename).encode())
		data = self.sockfd.recv(128).decode()
		if data == 'OK':
			try:
				fd = open(filename, 'rb')
			except IOError:
				print("No such file")
				return
			while True:
				data = fd.read(1024)
				if not data:
					time.sleep(0.1)
					self.sockfd.send(b'##')
					break
				self.sockfd.send(data)
			fd.close()
		else:
			print(data)
			
def main():
	sockfd = socket()

	try:
		sockfd.connect(ADDR)
	except Exception as e:
		print(e)
		return

	# 创建对象调用功能函数
	ftp = FtpClient(sockfd) # 当所有方法都需要一个参数时，将参数变为属性

	while True:
		print("\n----------------Order menu----------------")
		print("***                list                ***")
		print("***              get file              ***")
		print("***              put file              ***")
		print("***                quit                ***")
		print("------------------------------------------")

		cmd = input(">>")
		if cmd.strip() == 'list':
			ftp.do_list()
		elif cmd.strip() == 'quit':
			ftp.do_quit()
		elif cmd[:3] == 'get':
			filename = cmd.split(' ')[-1]
			ftp.do_get(filename)
		elif cmd[:3] == 'put':
			filename = cmd.split(' ')[-1]
			ftp.do_put(filename)
		else:
			print("Error")	

if __name__ == '__main__':
	main()