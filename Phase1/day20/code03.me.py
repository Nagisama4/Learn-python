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

result = filter(lambda _:_.score > 90 ,studs)
for i in result:
    print(i)

for item in sorted(studs, key = lambda _:_.score, reverse = True):
    print(item)