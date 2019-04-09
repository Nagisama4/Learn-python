# 订单管理用户接口层（视图层）
# 用于接收用户指令，显示执行结果

from order import *
from order_manage import *

orderManage = None               # 全局变量，订单管理对象

def print_menu(): #打印主菜单
    menu = '''
    --------------- 订单管理程序 ---------------
      1 - 查询所有订单      
      2 - 根据订单号查询
      3 - 新增订单
      4 - 修改订单         
      5 - 删除订单
      其它 - 退出
    '''
    print(menu)

def query_all():
    order_list = orderManage.query_all_order()
    for i in order_list:
        print(i)


def main():
    global orderManage
    orderManage = OrderManage()    # 实例化OrderManage
    while True:
        print_menu()
        oper = input("选择要执行的操作: ")
        if oper   == "1":
            query_all()
        elif oper == "2":
            pass
        elif oper == "3":
            pass
        elif oper == "4":
            pass
        elif oper == "5":
            pass
        else:
            break


main()