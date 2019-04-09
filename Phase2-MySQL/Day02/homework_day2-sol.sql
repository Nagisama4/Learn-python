-- homework_day2.sql
-- MySQL第二天作业

-- 1. 创建数据库bank, 并指定为utf8编码格式

-- 2. 创建账户表(acct, utf8编码格式), 包含如下字段
-- 	acct_no   	账号，字符串类型，长度32字符
-- 	acct_name 	户名，字符串类型，长度128字符
-- 	cust_no   	客户编号，字符串类型，长度32字符
-- 	acct_type	账户类型, 整数型(1-存款账户 2-贷款账户)
-- 	reg_date	开户日期, 日期类型
-- 	status		账户状态(1-正常 2-注销 3-挂失 4-冻结)
-- 	balance   	数字类型，最长16位，2位小数

-- 3. 至少插入五笔数据(要求数据尽量看上去真实) 

-- 4. 编写如下SQL语句 
-- 1)查找某个客户账户信息(以客户编号做条件)
-- 2)查找余额大于等于5000的账户信息
-- 3)查找余额大于等于5000的贷款账户信息
-- 4)查找账户名称以'D'开头的所有账户信息
-- 5)查找所有账户信息，并按照金额倒序排列
-- 6)统计每种状态的账户笔数
-- 7)查询账户余额的最大值、最小值、平均值、总金额
-- 8)查询账户余额最大的前3笔订单

-- 1. 
create database bank default charset=utf8;

-- 2.
create table acct(
	acct_no varchar(32),
	acct_name varchar(128),
	cust_no varchar(32),
	acct_type int unsigned,
	reg_date date,
	status int unsigned,
	balance decimal(16, 2)
) default charset=utf8;

-- 3.
insert into acct values
	('6287100001','Zhang','032800001',1,date(now()),1,1500000),
	('6287100002','Li','032800002',1,date(now()),1,300000),
	('6287100003','Wang','032800003',2,date(now()),1,3000000),
	('6287100004','Chen','032800004',1,date(now()),4,0),
	('6287100005','Xiao','032800005',2,date(now()),2,0),
	('6287100006','Ji','032800006',1,date(now()),3,4000),
	('6287100007','Ding','032800007',1,date(now()),2,0);

-- 4.
-- -- 1) 查找某个客户账户信息(以客户编号做条件)
select * from acct where cust_no like '%002';

-- -- 2) 查找余额大于等于5000的账户信息
select * from acct where balance > 5000;

-- -- 3) 查找余额大于等于5000的贷款账户信息
select * from acct where balance > 5000 and acct_type = 2;

-- -- 4) 查找账户名称以'D'开头的所有账户信息
select * from acct where acct_name like 'D%';

-- -- 5) 查找所有账户信息，并按照金额倒序排列
select * from acct order by balance desc;

-- -- 6) 统计每种状态的账户笔数
select acct_type, count(*) from acct group by acct_type;

-- -- 7) 查询账户余额的最大值、最小值、平均值、总金额
select max(balance) "最大金额",
 	   min(balance) "最小金额",
 	   avg(balance) "平均金额",
 	   sum(balance) "总金额"
 	from acct;

-- -- 8) 查询账户余额最大的前3笔订单
select * from acct order by balance desc limit 3;
