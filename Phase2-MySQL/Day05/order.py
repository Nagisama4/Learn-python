# 订单类：存放订单属性

class Order:
    def __init__(self, order_id, cust_id, product_num, amt):
        self.order_id = order_id
        self.cust_id  = cust_id
        self.product_num = product_num
        self.amt = amt

    def __str__(self):            # 重写__str__方法
        ret = "编号:%s,客户编号:%s,数量:%d,金额:%.2f"%(self.order_id, self.cust_id, self.product_num, self.amt)
        return ret