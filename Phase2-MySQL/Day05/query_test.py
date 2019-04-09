# pymysql 查询示例
# 导入PyMySQL模块
import pymysql
from db_conf import *

# 建立数据库连接

# 调用pymysql模块下connect函数连接数据库
# 连接成功后，返回一个连接对象，放到conn变量中
conn = pymysql.connect(host, user, passwd, dbname)

# 创建游标对象
cursor = conn.cursor()

# 使用游标对象提供的方法，执行SQL语句
sql = "select * from orders"
cursor.execute(sql)

# 取出所有数据
result = cursor.fetchall()
for row in result:
	order_id = row[0]
	cust_id = row[1]
	amt = row[5]
	print("订单编号：%s,编号：%s，金额：%s"%order_id, cust_id, amt)

# 提交事务（如果需要）
# 关闭游标
cursor.close()

# 关闭数据库
conn.close()