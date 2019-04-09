# 业务逻辑层 / 订单管理类
# 处理跟订单相关的逻辑操作, 调用DAO来实现数据存取

from order import *
from order_dao import *

class OrderManage:
    def __init__(self):                  # 实例化数据访问对象
        self.order_dao = OrderDAO()

    def query_all_order(self):           # 查询所有订单
        return self.order_dao.query_all_order()