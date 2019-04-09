# db_conf.py
# 导入PyMySQL模块
# 

# 建立数据库连接
host   = "localhost"
user   = "root"
passwd = "123456"
dbname = "eshop"

# 调用pymysql模块下connect函数连接数据库
# 连接成功后，返回一个连接对象，放到conn变量中
# conn = pymysql.connect(host, user, passwd, dbname)