Group chat model(simple version)

1. 确定技术模型

	[1] 消息的网络传输： socket --> UDP协议
	[2] 发送模型： 转发： 客户端 --> 服务端 --> 其他客户端
	[3] 服务端用户存储： 字典{name:address} 或 列表[(name, address),()]
	[4] 收发关系： 多进程，分别处理消息收发

2. 整体设计

	[1] 封装方法： 函数

3. 注意

	[1] 每个模块单独测试，写一个测试一个
	[2] 注释的添加

4. 具体实现

	[1] 网络连接搭建
	[2] 进入聊天室
		# 客户端：
			- 输入姓名
		    - 将姓名发送给服务端，添加首字段以区分请求类型
		    - 接收反馈
		    - OK则进入，否则重新输入
		# 服务端：
			- 接收姓名
			- 判断姓名是否存在（允许进入条件）
			- 不允许则结束，允许则将信息保存到数据字典
			- 将登陆信息广播告知其他人
	[3] 实现聊天
		# 客户端：
			- 创建子进程
				发送进程循环 input --> sendto
				接收进程循环 recvfrom
			- 发送内容至客户端，添加首字段以区分请求类型
		# 服务端：
			- 接收聊天内容，判断内容类型
			- 将内容转发至所有客户端
	[4] 退出聊天室
		# 客户端：
			- 输入quit退出，退出进程
		# 服务端：
			- 判断消息类型
			- 通知其他用户
			- 给该用户发送回文'EXIT'，并从字典中删除用户
	[5] 管理员公告