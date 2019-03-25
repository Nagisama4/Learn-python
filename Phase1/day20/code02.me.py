"""
    使用工具类操作学生列表
"""
class StudentModel:
    def __init__(self, id=0, name="", age=0, score=0):
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)" % (self.id, self.name, self.age, self.score)


studs = [
    StudentModel(101, "z01", 18, 85),
    StudentModel(102, "z02", 26, 55),
    StudentModel(103, "z03", 27, 75),
    StudentModel(104, "z04", 35, 90),
]
# -------------------------------------------------
from common.list_tools_me import ListHelper

def condition01(item):
    return item.age > 25

# 查找年龄大于25的所有学生对象
# re01 = ListHelper.find_all(studs, condition01)
# for item in re01:
#     print(item)

#练习1：将通用的查找所有对象方法，定义到common/list_tools_me.py/ListHelper
#练习2：ListHelper类中，定义通用的查找单个对象方法。
#     例如：查找年龄小于30的单个(第一个)学生对象
#     例如：查找姓名是z03的单个(第一个)学生对象

def condition01(item):
    return item.age < 30
def condition02(item):
    return item.name == "z03"
# def get_student01(list_stu):
#     for item in list_stu:
#         if item.age < 30:
#             return item
# def get_student02(list_stu):
#     for item in list_stu:
#         if item.name == "z03":
#             return item
# re01 = ListHelper.first(studs,condition02)
# print(re01)

# 练习：通用的计算满足某个条件的对象数量
# 例如：查找成绩大于80的学生数量
# 例如：查找姓名是z01的学生数量

def condition03(item):
    return item.score > 80

def condition04(item):
    return item.name == "z01"

# def get_count01(list_stu):
#     int_count = 0
#     for item in list_stu:
#         if item.score > 80:
#             int_count += 1
#     return int_count
#
# def get_count02(list_stu):
#     int_count = 0
#     for item in list_stu:
#         if item.name == "z01":
#             int_count += 1
#     return int_count
# ----------------------------------------------------------------
# re01 = ListHelper.count(studs,condition04)
# print(re01)


# re02 = ListHelper.count(studs, lambda _:_.score > 70)
# print(re02)


# re03 = ListHelper.first(studs, lambda _:_.id == 101)
# print("3",re03)

# for item in ListHelper.find_all(studs, lambda _:_.score < 60):
# 	print("4",item)

# for item in ListHelper.find_all(studs, lambda _:_.age > 20 and _.score > 60):
# 	print("5",item)

# ----------------------------------------------------------------

# def findmaxage(list_stu):
# 	max = list_stu[0]
# 	for i in range(1, len(list_stu)):
# 		if max.age < list_stu[i].age:
# 			max = list_stu[i]
# 	return max

# print(ListHelper.find_max(studs, lambda _:_.age))
# print(ListHelper.find_max(studs, lambda _:_.score))

# ----------------------------------------------------------------

# def addscore(list_stu):
# 	ssum = 0
# 	for i in list_stu:
# 		ssum += i.score
# 	return ssum

# print(addscore(studs))

# print(ListHelper.allsum(studs, lambda _:_.score))

# ----------------------------------------------------------------

# def get_allname(list_stu):
# 	for i in list_stu:
# 		yield i.name

# for i in get_allname(studs):
# 	print(i)

# for i in ListHelper.obtain_element(studs, lambda _:_.name):
# 	print(i)

# for i in ListHelper.obtain_element(studs, lambda _:_.score):
# 	print(i)

# ----------------------------------------------------------------

def order_by_score(list_stu):
    for r in range(len(list_stu) - 1):
        for c in range(r + 1, len(list_stu)):
            if list_stu[r].score > list_stu[c].score:
                list_stu[r], list_stu[c] = list_stu[c], list_stu[r]
    return list_stu

for i in order_by_score(studs):
	print(i)

for i in ListHelper.high_sort(studs, lambda _:_.score):
	print(i)

# ----------------------------------------------------------------

