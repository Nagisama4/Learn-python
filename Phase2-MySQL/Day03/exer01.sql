select orders.order_id, orders.amt,
	customer.cust_name, customer.tel_no
	from orders, customer;
-- 联合查询，笛卡尔积为结果，条件不紧密，结果会有问题

-- 内连接 用where限定条件
select orders.order_id, orders.amt,
	customer.cust_name, customer.tel_no
	from orders, customer
	where orders.cust_id = customer.cust_id;

-- 内连接 用inner join关键字
select orders.order_id, orders.amt,
	customer.cust_name, customer.tel_no
	from orders inner join customer
	on orders.cust_id = customer.cust_id;

select a.order_id, a.amt,
	b.cust_name, b.tel_no
	from orders a inner join customer b
	on a.cust_id = b.cust_id;
-- 简化写法，简化表名

select a.order_id, a.amt,
	b.cust_name, b.tel_no
	from orders a left join customer b
	on a.cust_id = b.cust_id;
-- 左连接 

select a.order_id, a.amt,
	b.cust_name, b.tel_no
	from orders a right join customer b
	on a.cust_id = b.cust_id;
-- 右连接

create table orders_detail(
	order_id varchar(32),
	product_id varchar(128),
	amt decimal(16, 2)
) default charset=utf8;

insert into orders_detail values
	('201901010001','apt-0001',100),
	('201801010003','apt-0003',100),
	('201801010004','apt-0004',100),
	('201801010006','apt-0006',98);

select orders.order_id, orders.order_date,
	customer.cust_name,
	orders_detail.product_id, orders_detail.amt
	from orders, customer, orders_detail
	where orders.order_id = orders_detail.order_id and customer.cust_id = orders.cust_id;

create table t1(
	stu_no varchar(32) primary key,  -- 主键
	stu_name varchar(32) not null,   -- 非空
	id_card_no varchar(32) unique    -- 唯一
);

insert into t1 values
	('001','Jenifer','51382219900101111111');

insert into t1 values
	('002',null,'51382219900101111112');     -- 空值报错

insert into t1 values
	('002','ewae','51382219900101111111');   -- 重复报错

insert into t1(stu_no, stu_name) values
	(null, 'dewa');                          -- 主键空值报错

insert into t1(stu_no, stu_name) values
	('001', 'dewa');                         -- 主键重复报错

create table t2(
	id int primary key auto_increment,  -- 自动增长必须设置主键
	name varchar(32),
	status int default 0
);

insert into t2 values(NULL,'Jerry',1);

insert into t2 values(NULL,'Tom',2);

insert into t2(id,name) values(NULL,'Henry');

create table course(
	course_id varchar(32) primary key,
	name varchar(32)
);

create table teacher(
	id int auto_increment primary key,
	name varchar(32),
	course_id varchar(32),
	constraint fk_course foreign key(course_id)
	references course(course_id)   -- 外键约束
);

insert into course values('0001','Python');

insert into teacher values(1,'Jerry','0001');

delete from course where course_id = '0001';

create table t6(
	id int,
	name varchar(32),
	status int,
	course_id varchar(4),
	tel_no varchar(32)
);

alter table t6 add primary key(id);
alter table t6 modify id int auto_increment;
alter table t6 modify status int default 0;
alter table t6 modify tel_no varchar(32) unique;
alter table t6 add constraint fk_course_id foreign key(course_id) references course(course_id);

select * from orders into outfile '/var/lib/mysql-files/orders.csv'
fields terminated by ','
lines terminated by '\n';

sudo cat /var/lib/mysql-files/orders.csv

load data infile '/var/lib/mysql-files/orders.csv' into table orders
fields terminated by ','
lines terminated by '\n';

create table orders_new select * from orders;
-- 将orders数据，表结构全部复制到新表

create table orders_new select * from orders where 1 = 0;

alter table orders rename to orders_bak;