
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

update orders set status = 2
	where order_id = '201801010001';

select * from orders where status <> 2;

select * from orders where amt between 200 and 300;

select * from orders where cust_id in ('c0002','c0005');

select * from orders where cust_id not in ('c0003','c0004');

create table customer(
	cust_id varchar(32),
	cust_name varchar(32),
	tel_no varchar(32)	
) default charset=utf8;

insert into customer values
	('c0001','Jerry','13512345678'),
	('c0002','Dekie','13522334455'),
	('c0003','Dokas','15844445555');

select * from customer where cust_name like 'D%'; 
-- 查找以D开头的姓名

select * from customer where tel_no like '%44%55%'; 
-- 模糊查询 查找字段中包含44和55的，可以在任意位置

select * from customer where tel_no is NULL; //is not NULL;
-- 查询某字段是否为空//不为空

select * from customer order by amt desc; 
-- 降序， asc 升序

limit n    -- 只显示前面n笔
limit m,n  -- 从第m笔开始，总共显示n笔

select * from customer limit 2;

select * from orders order by amt desc limit 2;
-- 先排序，再显示前两条

insert into customer values
	('c0004','Jerry','13512345678'),
	('c0005','Dekie','13522334455'),
	('c0006','Dokas','15844445555'),
	('c0007','Dokas','15844891155'),
	('c0008','Dokas','15844415615'),
	('c0009','Dokas','15844165555'),
	('c0010','Dokas','15813145555');

-- 简单分页查找
select * from customer limit 0, 3;

select * from customer limit 3, 3;

select * from customer limit 6, 3;

select * from customer limit 9, 3;

select distinct(cust_name) from customer;
-- 字段查重

select max(amt) "最大金额",
 	   min(amt) "最小金额",
 	   avg(amt) "平均金额",
 	   sum(amt) "总金额"
	from orders;

select count(*) from orders;
-- 统计笔数

select count(*) from customer where tel_no like '135%';
-- 条件查询

select cust_name, count(*) from customer group by cust_name;
-- 按某字段分组

select status, sum(amt) from orders group by status;
-- 分组统计

select status, sum(amt) from orders group by status having sum(amt) > 500;
-- 分组统计，保留满足条件结果 having
-- 说明： group by分组聚合的结果，只能用having，不能用where，where只能用户表中有的字段作为条件的时候
 
create table student(
	stu_no varchar(32),
	stu_name varchar(128)
);

alter table student add age int;
-- 添加字段，默认最后
alter table student add id int first;
-- 添加字段放在最前
alter table student add tel_no varchar(32) after stu_name;
-- 添加字段放在某字段后

alter table student modify stu_name varchar(64);
-- 修改字段长度

alter table student change age stu_age int;
-- 更改字段名称

alter table student drop id;
-- 删除字段