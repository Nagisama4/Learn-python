ftp文件服务

   1. 功能
	    [1] 分为服务端和客户端，要求可以多个客户端同时操作
		[2] 客户端可以查看服务器中有哪些文件(普通文件，不包含隐藏的)
		[3] 客户端可以从服务器下载文件到本地目录下
		[4] 客户端可以将本地文件上传的服务端
		[5] 在客户端中端打印简单的命令提示界面
	
   2. 技术分析   
		[1] 使用fork多进程并发
		[2] tcp套接字
		[3] 筛选文件库文件
		    -- os.listdir()  获取目录下文件列表
			-- os.path.isfile() 判断一个文件是否为普通

   3. 结构设计
		 
	客户端：
	  	[1] 客户端启动后先进行网路连接打印界面
		[2] 客户端选择执行的功能进行执行

    服务端：
		[1] 搭建fork并发网络结构等待连接
		[2] 使用子进程循环接收请求处理请求

    请求响应流程： 客户端发起请求-->服务端请求判断能否执行，给客户端反馈-->如果能够执行则进行具体操作

	封装：将2,3,4功能封装为一个类，分别通过方法实现。网络搭建写在main中

   4. 具体功能模块
	  
		* 搭建网络连接
		* 查看文件列表
		* 下载文件
		* 上传文件
		* 客户端退出