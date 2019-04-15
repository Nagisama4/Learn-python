"""
FTP 服务器
fork 并发
"""

from socket import *
import os,sys
import signal
import time

# Global variables
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)
FILE_PATH = '/home/tarena/桌面/net/ftp/'

class Ftpserver(object):
	def __init__(self, connfd):
		self.connfd = connfd

	def do_list(self):
		# 获取文件列表
		file_list = os.listdir(FILE_PATH)
		if not file_list:
			self.connfd.send("library is empty".encode())
			return
		else:
			self.connfd.send(b'OK')
			time.sleep(0.1)

		files = ""
		for file in file_list:
			if file[0] != '.' and os.path.isfile(FILE_PATH + file):
				files += file + "#"

		self.connfd.send(files.encode())

	def do_get(self, filename):
		try:
			fd = open(FILE_PATH + filename, 'rb')
		except IOError:
			self.connfd.send('No such file'.encode())
			return
		else:
			self.connfd.send(b'OK')
			time.sleep(0.1)
		# send file
		while True:
			data = fd.read(1024)
			if not data:
				time.sleep(0.1)
				self.connfd.send(b'##')
				break
			self.connfd.send(data)
		fd.close()

	def do_put(self, filename):
		fd = open(FILE_PATH + filename, 'wb')
		self.connfd.send(b'OK')
		while True:
			data = self.connfd.recv(1024)
			if data == b'##':
				break
			fd.write(data)
		fd.close()


def do_request(connfd):
	ftp = Ftpserver(connfd)
	while True:
		data = connfd.recv(1024).decode()
		if not data or data[0] == 'Q':
			connfd.close()
			return
		elif data[0] == 'L':
			ftp.do_list()
		elif data[0] == 'G':
			filename = data.split(' ')[-1]
			ftp.do_get(filename)
		elif data[0] == 'P':
			filename = data.split(' ')[-1]
			ftp.do_put(filename)


# Network build
def main():
	sockfd = socket()
	sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sockfd.bind(ADDR)
	sockfd.listen(5)

	signal.signal(signal.SIGCHLD, signal.SIG_IGN)
	print("Listen the port 8888...")

	while True:
	    try:
	        connfd, addr = sockfd.accept()
	    except KeyboardInterrupt:
	        sys.exit("Exit from server")
	    except Exception as e:
	        print(e)
	        continue
	    print("Connect from ", addr)

	    # Build child processes
	    pid = os.fork()
	    if pid == 0:
	        sockfd.close()    # 子进程不需要s端
	        do_request(connfd)
	        os._exit(0)
	    else:
	        connfd.close()    # 父进程不需要c端

if __name__ == "__main__":
	main()