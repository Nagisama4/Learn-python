课程：MySQL关系型数据库
进度：day1
邮件：g-wangdb@tedu.cn

主要内容：
1. 数据库的相关概念
2. MySQL安装、配置
3. 库管理
4. 表管理
5. 结构化查询语言（SQL）
6. 数据约束：数据要遵循的规则
7. 数据导入、导出
8. 权限管理
9. 数据库事务
10.存储引擎
11.E-R概念模型（设计相关）
12.Python访问数据库

特点：
1. 入门容易，提高难
2. 知识点多，小，零散
3. 看不见内部实现

总体目标
1. 理解、掌握关系数据库的理论、概念
2. 熟练掌握SQL语言
3. 熟练掌握MySQL日常使用
4. 掌握权限、备份、恢复日常管理工作
5. E-R概念模型
6. 熟练应用Python访问MySQl数据库

为什么要学数据库
1. 数据库是软件人员必备技能
2. 软件离开数据库没法实现（数据高速存取）
3. 数据库管理可以作为长期职业发展方向（DBA，数据库专家）

今天的内容
1. 什么是数据库(Database)：根据一定模型（理论依据），集中对数据进行管理的仓库
2. 数据库管理系统（Database Management System, 简写DBMS）：专门用于数据管理的软件系统，位于操作系统和用户之间的数据管理系统
3. 数据库系统：DBMS，硬件/软件，应用程序，用户

DBMS应用场合
1)银行中客户，账户，交易信息存储
2)电商系统中商品、订单、客户信息存储
3)仓库关系统中的数据存储
......

重要概念(重点)
1）关系：规范的二维表
2）关系型数据库：使用关系模型的数据库
   二维表表示数据、数据之间的联系
	 关系型数据库用来处理结构化数据
3）实体：现实中可以区分的事物
4）元组：二维表中的一行，描述一个实体信息
5）属性：实体的某个数据特征
6）键：可以区分实体的属性、属性组合
7）主键：从键中选取一个，作为逻辑上唯一区分实体的依据

windows下安装（见讲义）

ubuntu下安装
1. sudo apt-get install mysql-server
   说明：apt-get是一个在线软件管理工具，能够在线安装、删除、升级软件的版本
   apt-get install：执行安装操作
2. 安装确认
1）指令：netstat -an | grep 3306
   说明：grep是过滤指令
2）通过脚本查看
	sudo /etc/init.d/mysql  [参数]
	status: 查看服务状态
      start:  启动服务
      stop: 停止服务
      restart: 重启服务
3. 查看配置文件
   cd /etc/mysql/conf.d
	 cat mysql.cnf
	 说明：cat是查看文件内容

MySQL相关目录
/usr/bin                可执行文件    
   ls /usr/bin/mysql*
/var/lib/mysq           存放数据
   ls 
/etc/init.d/mysql       服务管理脚本
   vim -R /etc/init.d/mysql
	 :q!   强制退出vim
/etc/mysql              数据库服务器配置

sudo -i    直接切换到root用户
exit       退出当前用户

库管理
1. 查看库：show databases;
2. 创建库：
1)语法：create database 库名称 [字符集] 
2)示例：创建一个名称为eshop的库
  create database eshop
  default charset=utf8;
3)库的命名规则
  可以使用数字、字母、下划线
  不能使用纯数字
  库名区分大小写
  库名必须唯一
  不能使用特殊字符和MySQL关键字
3.进入库/切换库
  USE 库名称
  例：use eshop; 
4.查看库
  1）查看当前库：select DATABASE();
  2）查看某个库建库的语句
    show CREATE DATABASE 库名
	如：show CREATE DATABASE eshop;
  3）查看库中有哪些表
    show tables;

5. 删除库
  DROP DATABASE 库名
  例：drop DATABASE eshop;

表管理（重点内容）
1.创建表
  1）建表之前，要进入库
  2）建表语法
    CREATE TABLE 表名称(
	  字段1 类型(长度) 约束,
      字段2 类型(长度) 约束,
      ......
	)[字符集];
  3）创建订单表
    CREATE TABLE orders(
	  order_id VARCHAR(32),
	  cust_name VARCHAR(64)
	) default charset=utf8;
	执行成功后，再查看：show tables;
 2. 查看表结构
   1)查看表结构：desc 表名称;
     例：desc orders;
   2)查看建表语句：show create TABLE 表名
     例：show CREATE TABLE orders;
3. 删除表
   1)语法：drop TABLE 表名
   2)示例：drop TABLE orders;

4. 示例：创建订单表
  CREATE TABLE orders(
    order_id VARCHAR(32),  -- 订单编号
	cust_id VARCHAR(32),   -- 客户编号
	order_date datetime,-- 下单时间，日期时间类型
    status int,         -- 状态
	products_num INT,   -- 商品数量，整数
	amt DECIMAL(16,2)   -- 订单总金额
	                    -- 最长16位，小数2位
  ) DEFAULT charset=utf8;
  容易出错的地方：
  SQL中出现中文符号；括号匹配不正确；
  date不是data；最后一个字段后面没有分号

表记录管理（重点内容）
1. 插入记录
  1)所有字段都插入值
  INSERT INTO orders VALUES
  ('201801010001','C0001',now(),1,1,100.00);
  
  查询：select * FROM orders;
  说明：
    values后面没有指定字段，表示插入所有
	值列表个数、顺序、类型要和表结构严格对应
	字符串类型必须要单引号引起来
	now()函数表示取数据库当前时间
  2) 向表中插入指定字段值
    语法：insert INTO 表(字段列表)
	      VALUES(值列表)
	示例：
	  insert INTO orders(order_id, cust_id)
	  VALUES('201801010002', 'C0002');
  3)一个SQL语句插入多笔数据
    INSERT INTO orders VALUES
	('201801010003','C0003',now(),1,1,200.00),
	('201801010004','C0004',now(),1,1,480.00);

2. 查询记录
  1)语法格式
    SELECT * FROM 表名 [WHERE 条件];

	SELECT 字段1, 字段2...
	FROM 表名 [WHERE 条件];
  2)示例
    - 查询表中所有数据
	  SELECT * FROM orders;
	- 查询订单编号、客户编号
	  SELECT order_id, cust_id FROM orders;
    - 查询指定字段，给每个字段起个别名
	  SELECT order_id "订单编号", 
	         cust_id "客户编号"
	  FROM orders;
	- 带一个条件的查询
	  SELECT * FROM orders 
	  WHERE order_id = '201801010003';

	- 带多个条件的查询
	  SELECT * FROM orders
	  WHERE order_id = '201801010003'
	  AND status = 1; 
	  -- AND表示两个条件同时满足
	  -- OR表示满足其中一个



