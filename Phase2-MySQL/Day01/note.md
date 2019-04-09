sudo /etc/init.d/mysql start    //启动MySQL
sudo /etc/init.d/mysql status   //查看状态
sudo /etc/init.d/mysql stop     //停止服务
sudo /etc/init.d/mysql restart  //重启服务

mysql -uroot -p                 //进入，密码123456

create  database 库名
default charset=utf8;           //建库

use eshop;                      //进入库
select database();              //查看当前库
show tables;                    //查看库中表
drop database 库名;             //删除库

show create database 库名;      //查看创建库的语句

#------------------------------------------------------------------#
//表管理, 建表前先进库

create table 表名(
  字段1 类型(长度) 约束,
  字段1 类型(长度) 约束,
  ......
)[字符集];

#------------------------------------------------------------------#
example:

create table orders(
  order_id varchar(32), -- 订单编号
  cust_name varchar(64)
) default charset=uft8;

#------------------------------------------------------------------#

desc 表名;                      //查看表信息
show create table 表名;         //查看创建表的语句
drop table 表名;                //删除表

#------------------------------------------------------------------#
//表记录管理
insert into 表名 values
('201801010001','c0001',now(),1,1,100.00);        //所有字段都插入值

select * from 表名              //查询表内容

insert into 表名(字段列表)
values(值列表);

insert into orders(order_id, cust_id)
values('201801010002','c0002');               //插入特定字段

insert into orders values
('201801010003','c0003',now(),1,1,100.00),
('201801010004','c0004',now(),1,2,200.00),
('201801010005','c0005',now(),1,3,340.00),
('201801010006','c0006',now(),1,5,490.00);    //插入多段数据

//查询记录
select * from 表名 where 条件 [and 条件] [or 条件];   //查询所有

select 字段1,字段2...                         
from 表名 [where 条件];                       //查询特定字段

select 字段1 "Nick name",字段2 "nick name"...
from 表名 [where 条件];                       //查询特定字段并起别名

#------------------------------------------------------------------#

create talbe num_test(
	type int(3) unsigned zerofill,
	rate decimal(10,2)
	-- type 是整数型，存储实际空间是4Bytes
	-- 大小是由数据类型决定的
	-- int(3) 表示默认显示3位
	-- unsigned 表示无符号（0和整数）
	-- zerofill 表示左边用0填充
);

insert into num_test values
(1, 0.88),
(2, 123.456),
(3, 2),
(1000, 3.444);

#------------------------------------------------------------------#

create table enum_test(
	name varchar(32),
	sex  enum('boy','girl'),
	course set('music','dance','paint')
);

insert into enum_test values
('Jerry','boy','music,dance');

insert into enum_test values
('Tom','boy','music,footboy');

insert into enum_test values
('Tom','female','music');

select now(), sysdate();
select curdate(), curtime();
select year(now()), month(now()), day(now());