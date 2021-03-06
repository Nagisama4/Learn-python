前情回顾

1. multiprocessing 模块创建进程

   Process(target,args,kwargs)  创建进程对象
	 p.start()  启动进程
	 p.join()  回收进程

2. 进程对象属性
	 p.name  p.pid  p.is_alive()   p.daemon

3. 自定义进程类：继承Process  重写 __init__,run

4. 进程池：当有大量的小任务需要多进程完成，进程池可以避免频繁的创建销毁进程带来的资源消耗。

   Pool()  创建进程池
	 apply_async() 将事件加入进程池执行
	 close()  关闭进程池
	 join()  回收进程池

5. 进程间通信

  管道 ： Pipe()  fd.recv()  fd.send()
**************************************************

一. 进程间通信（续）

  1. 消息队列
	  
		【1】通信原理：在内存中建立队列模型，进程通过队列存取消息实现通信

		【2】实现方法

		  from multiprocessing import Queue
			
			q = Queue(maxsize = 0)
			功能 ： 创建消息队列
			参数 ： 最多存放多少个消息

			q.put(data,[block,timeout])
			功能： 向队列存入消息
			参数： data  要存入的内容
						 block  False 为非阻塞
						 timeout  超时时间
			
			data = q.get([block,timeout])
			功能: 从队列中取出消息
			参数：block  False 为非阻塞
						timeout  超时时间
			
			q.full() 判断队列是否为满
			q.empty()  判断队列是否为空
			q.qsize()  获取队列中消息个数
			q.close()  关闭队列
	

	2. 共享内存
	  
		【1】 通信原理：在内存中开辟一块空间，进程可以写入和读取内容，但是每次写入内容都会覆盖之前内容

		【2】 实现方法
		  
			from multiprocessing import Value,Array

			obj = Value(ctype,data)
			功能: 创建共享内存
			参数: ctype  共享内存类型  'i'  'f'  'c'
						data   共享内存初始数据
			
			obj.value 对该属性修改查看即共享内存读写


			obj = Array(ctype,data)
			功能： 创建共享内存
			参数： ctype 共享内存类型
			       data  列表表示共享内存初始数据，整数表示共享内存开辟数据元素个数

			obj进行遍历或者索引方式获取值，也可以通过索引直接赋值
			
			obj.value 用于整体打印共享内存中字节串


  3. 信号量（信号灯集）

	【1】通信原理：给定一个数量对多个进程可见，多个进程都可以操作数量的增减，并根据数量决定行为

    【2】 实现方法

		  from multiprocessing import  Semaphore

			sem = Semaphore(num)
			功能：创建信号量对象
			参数： 信号量初始值
			返回值： 信号量对象

			sem.acquire()  消耗一个信号量，当信号量为0时会阻塞

			sem.release()  增加一个信号量

			sem.get_value()  获取信号量值

     注意：当在父进程中创建对象（文件对象，套接字对象，进程间通信对象），子进程从父进程中拷贝对象时父子进程对该对象的使用会有属性的相互影响。如果在父子进程中各自创建，则无影响。


二. 线程编程 （Thread）

  1.  什么是线程
	  
		【1】 线程被称为轻量级的进程
		【2】 线程也是多任务编程方法，可以使用计算机多核资源
		【3】 线程是系统分配内核的最小单元
		【4】 线程可以理解为进程中的任务分支程序

  2. 线程特征
	  
		【1】 一个进程可以包含多个线程
		【2】 线程也是一个运行过程，消耗计算机资源
		【3】一个进程中的所有线程共享这个进程资源
		【4】多个线程运行互不影响，各自执行
		【5】线程的创建和消耗消耗资源远小于进程
		【6】线程也有自己的特有属性特征命令集，id等

	
	3. threading模块创建线程

	  【1】 创建线程对象

		 from threading import Thread 

		 t = Thread()
		 功能: 创建线程对象
		 参数：target 绑定的线程函数
					 arges 元组  给线程函数位置传参
					 kwargs 字典 给线程函数关键字传参
		 
		【2】 启动线程
		  t.start()

		【3】 阻塞等待回收线程
		  t.join([timeout])

  4. 线程对象属性
	   
		 t.name  线程名称
		 t.setName()  设置线程名称
		 t.getName()  获取线程名称
	
	   t.is_alive()  查看线程是否在生命周期
			
		 t.daemon  设置主线程和分支线程的退出关系
		 t.setDaemon()  设置daemon属性值
		 t.isDaemon()  查看daemon属性值
		 * 设置daemon为True 此时主线程退出分支线程也会退出。设置在start前完成，不和join同用

  5. 自定义线程类

    【1】 创建步骤
		    1. 继承Thread类
				2. 重写init 方法添加自己的属性，执行父类init
				3. 重写run方法
		 
		【2】 使用
		    1. 实例化对象
				2. 调用start自动执行run
				3. join回收线程


三. 线程通信
 
   【1】 通信方法：线程间使用全局变量进行通信

	 【2】 共享资源的争夺
	   
		  1. 共享资源：多个进程或者线程都可以操作的资源称为共享资源

			2. 影响：对共享资源的无序操作可能会带来数据的混乱或者操作错误。此时需要同步互斥机制处理

      3. 同步互斥机制

			   同步：同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤执行操作。

				 互斥：互斥是一种制约关系，当一个进程或者线程抢占到资源时进行加锁处理，其他进程线程就无法操作资源，直到解锁后才能操作

      4. 线程互斥方法

			  1. 线程Event

				  from threading  import Event 
					
					e = Event()  创建event对象

					e.wait([timeout]) 阻塞等待直到e被set

					e.set() 设置e ，使wait结束阻塞

					e.clear() 清除e的设置，wait会阻塞

					e.is_set()  判断e的状态
 

作业 ： 1. 效率测试，记录时间
				2. 对比进程线程的特点联系和区别
				3. 复习socket重点程序



