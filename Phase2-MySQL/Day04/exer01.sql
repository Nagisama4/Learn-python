-- 在name上创建普通索引， 在cert_no上创建唯一索引

create table index_test(
	id int primary key,
	cert_no varchar(32),
	name varchar(32),
	unique(cert_no), index(name)
);

show index from index_test;

insert into index_test values
	(1, '0001', 'Jrwee');

insert into index_test values
	(2, '0001', 'Jrwee');          -- cert_no 违反约束

drop index cert_no on index_test;
drop index name on index_test;     -- 删除约束

create unique index idx_cert_no on index_test(cert_no);
-- 在index_test表cert_no字段创建唯一索引

-- 索引的效率测试
create index idx_order_id on orders(order_id);

explain select * from orders where order_id = '201801010000001';

create table acct(
	acct_no varchar(32),
	acct_name varchar(32),
	balance decimal(16,2)
);

insert into acct values
	('0001','Jerry',1000),
	('0002','Tom',2000);

-------------------------------------------------------
start transaction;               -- 数据库事务

update acct set balance = balance - 100
	where acct_no = '0001';

update acct set balance = balance + 100
	where acct_no = '0002';

commit;   -- 提交
rollback; -- 或回滚
-------------------------------------------------------

grant select on eshop.* to 'Tom'@'%' identified by '123456';
-- 授予权限

flush privileges;
-- 刷新权限

select * from mysql.db where User='Tom'\G;
-- 查看用户Tom权限

grant select, update, delete on eshop.* to 'Jerry'@'localhost' identified by '123456';

select * from mysql.db where User='Jerry'\G;

revoke delete on eshop.* from 'Jerry'@'localhost';
-- 删除权限

show grants;
-- 查看自己的权限

show grants for 'Tom'@'%';
-- 查看别人的权限




























