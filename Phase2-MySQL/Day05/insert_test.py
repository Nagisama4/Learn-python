# pymysql 查询示例
# 导入PyMySQL模块
import pymysql
from db_conf import *

# 调用pymysql模块下connect函数连接数据库
# 连接成功后，返回一个连接对象，放到conn变量中
conn = pymysql.connect(host, user, passwd, dbname)
# sql = '''insert into orders(order_id, cust_id) values
# 			('201801010010','C0010')'''

sql = '''delete from orders where order_id = '201801010010' '''

cursor.execute(sql)
conn.commit
cursor.close()
conn.close()