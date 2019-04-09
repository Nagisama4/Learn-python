create database eshop default charset=utf8;

CREATE TABLE orders(
    order_id VARCHAR(32),
	cust_id VARCHAR(32),
	order_date datetime,
    status int,
	products_num INT,
	amt DECIMAL(16,2)
  ) DEFAULT charset=utf8;

INSERT INTO orders VALUES
('201801010001','C0001',now(),1,1,100.00),
('201801010003','C0003',now(),1,1,200.00),
('201801010004','C0004',now(),1,1,480.00);
 

CREATE TABLE customer(
    cust_id VARCHAR(32),
	cust_name VARCHAR(32),
	tel_no VARCHAR(32)
) DEFAULT charset=utf8;

INSERT INTO customer VALUES
('C0001','Jerry','13512345678'),
('C0002','Dekie','13522334455'),
('C0003','Dokas','15844445555');