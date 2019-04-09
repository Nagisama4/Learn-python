# 订单数据访问对象 Data Access Object
# 拼装各种SQL语句，调用DBHelper的对象，实现数据库的操作

from order import *
from db_helper import *

class OrderDAO:
    def __init__(self):                    # 构造函数
        self.db_helper = DBHelper()        # 创建,持有DBHelper()
        self.db_helper.open_conn()         # 打开连接数据库

    def __del__(self):                     # 析构函数,对象销毁时调用
        self.db_helper.close_conn()

    def query_all_order(self):             # 查询所有订单, 返回订单对象列表
        sql = "select * from orders"
        order_list = []                    # 订单对象列表
        result = self.db_helper.do_query(sql)   # result返回元组
        if not result:
            print("There is no such thing")
            return None

        for i in result:
            order_id = i[0]
            cust_id  = i[1]
            if i[4]:
                product_num = int(i[4])
            else:
                product_num = 0
            if i[5]:
                amt = float(i[5])
            else:
                amt = 0.00
            order_list.append(Order(order_id, cust_id, product_num, amt))
        return order_list