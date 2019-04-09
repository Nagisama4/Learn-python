show engines;

show create table orders;

alter table 表名 engine = 引擎

create table t3(
	id int primary key,
	name varchar(32)
) engine = InnoDB;

alter table t3 engine = MyISAM;

show global variables like '%datadir%';

alter table t3 engine = Memory;

insert into t3 values(1,'Jerry');

