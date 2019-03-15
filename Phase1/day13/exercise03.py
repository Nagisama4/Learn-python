"""
    1. 定义学生类(姓名，成绩)

    2. 定义根据名称，查找学生对象的方法。
       def xxx(list_stu,stu_name):
          ......

    3. 创建3个学生对象并加入到列表中，指定不同的名字与成绩。
       再调用第二步的方法
"""


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def print_self(self):
        print(self.name, self.score)


def get_student_by_name(list_stu, stu_name):
    for item in list_stu:
        if item.name == stu_name:
            return item
            # return None


def get_student_by_id(list_stu, stu_id):
    # 遍历学生列表
    for item in list_stu:
        # 判断每个学生对象的编号 是否与 需要查找的编号相同
        if item.id == stu_id:
            # 返回学生对象
            return item

#practise: Searching for the student whose score is high than 90.

def get_student_by_score(list_stu, stu_score):
    result = []
    for item in list_stu:
        if item.score >= stu_score:
            result.append(item)
    return result


#practise2: Searching for the student who has the highest score.
#排序算法

def get_student_highest(list_stu):
    highest = list_stu[0]
    result = []
    for i in range(1, len(list_stu)):
        if highest.score <= list_stu[i].score:
            highest = list_stu[i]
            result.append(highest)
##        elif highest.score == list_stu[i].score:
##            result.append(list_stu[i])
    return result


#practise3: 查找列表中指定姓名的同学，同名也要
def get_student_by_name_forall(list_stu, stu_name):
    result = []
    for item in list_stu:
        if item.name == stu_name:
            result.append(item)
    return result

#practise4: 排序，按成绩高低
def sort_student_by_score(list_stu):
    result = []
    highest = list_stu[0]
    for r in range(len(list_stu) - 1):
        for c in range(r + 1, len(list_stu))：
            if list_stu[r].score < list_stu[c].score:
                list_stu[r], list_stu[c] = list_stu[c], list_stu[r]



list_stu = [
    Student(101, "zs", 86),
    Student(106, "we", 98),
    Student(102, "ls", 32),
    Student(103, "ww", 90),
    Student(104, "ld", 100),
    Student(105, "dw", 100),
    Student(107, "ld", 30),
]

##result = get_student_by_score(list_stu, 90)
##for item in result:
##    item.print_self()

##result = get_student_highest(list_stu)
##for item in result:
##    item.print_self()

# sname = get_student_by_name_forall(list_stu, "ld")
# for item in sname:
#     item.print_self()


sort_student_by_score(list_stu)
for item in list_stu:
    item.print_self()