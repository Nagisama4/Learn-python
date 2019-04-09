create table orders(
  order_id varchar(32), -- 订单编号
  cust_id varchar(32),  -- 客户编号
  order_date datetime,  -- 下单时间, 日期时间
  status int,  -- 状态
  products_num int,  -- 商品数量，整数
  amt decimal(16,2)  -- 订单总金额
  					 -- 最长16位，小数2位
) default charset=uft8; 


insert into orders values
	('201801010001','c0001',now(),1,1,100.00);

insert into orders values
	('201801010003','c0003',now(),1,1,100.00),
	('201801010004','c0004',now(),1,2,200.00),
	('201801010005','c0005',now(),1,3,340.00),
	('201801010006','c0006',now(),1,5,490.00);

select * from orders where order_id = '201801010004' and status = 1;