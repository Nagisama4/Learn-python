"""
    扩展案例：只适用于有基础同学
"""

list01 = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"],
]

# 需求：获取指定位置上的，某个方向，  指定数量的元素。
#          "20"      右侧0    1     3   ---> "21", "22", "23"
#          "31"      上方-1   0     2   ---> "21", "11"
#          "24"      左侧0    -1    4   ---> "23", "22", "21","20"
#          "03"      下方1    0     3   ---> "13", "23", "33"


# 面向过程方法：
# 拆分元素为坐标表示，上下左右移动方向为坐标移动
"""
def get_elements(list_target, r_index, c_index, r_dir, c_dir, count):
    result = []
    for i in range(count):
        r_index += r_dir#2  += 0   2  += 0   2 += 0
        c_index += c_dir#0  += 1   1  += 1   2 += 1
        result.append(list_target[r_index][c_index])
    return result

# 缺点1：代码可读性差
#    2：每次调用方法，都需要思考方向(索引变化)的特征
print(get_elements(list01,2,0,0,1,3))
print(get_elements(list01,3,1,-1,0,2))
"""

# 面向对象方法：
# 解决：使用一个类，包装两个数据(行/列)
class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def right(self):
    #     return Vector2(0, 1)

    @staticmethod  #  静态方法：不依赖于对象与类
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)


def get_elements(list_target, vect_pos, vect_dir, count):
    result = [] #空列表不显示原始位置
#    result = [list_target[vect_pos.x][vect_pos.y]] #列表初始显示原始位置
    for i in range(count):
        vect_pos.x += vect_dir.x  # 2  += 0   2  += 0   2 += 0
        vect_pos.y += vect_dir.y  # 0  += 1   1  += 1   2 += 1
        result.append(list_target[vect_pos.x][vect_pos.y])
    return result


print(get_elements(list01, Vector2(2, 3), Vector2.up(), 1))
print(get_elements(list01, Vector2(1, 1), Vector2.down(), 1))
print(get_elements(list01, Vector2(0, 4), Vector2.left(), 1))
print(get_elements(list01, Vector2(2, 3), Vector2.right(), 1))
