class StudentModel:
    """
    数据模型类
    """
    def __init__(self, id = 0, name = "", age = 0, score = 0):
        """
        :param:id     编号
        :param:name   姓名
        :param:age    年龄
        :param:score  成绩
        """
        self.id    = id
        self.name  = name
        self.age   = age
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
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    """
    逻辑控制类
    """
    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu
    
    def generate_id(self,id):
        # 生成编号策略：在最后一个学生编号基础上增加1
        #             如果是第一个学生，则设置为1
        # if语句的真值表达式
        return 1 if len(self.__list_stu) == 0 else self.__list_stu[-1].id + 1

    def remove_student(self,id):
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                return True # 表达删除成功
        return False # 表达删除失败

    def update_student(self,stu_info):
        # 需要修改的学生编号： stu_info.id
        # 需要修改的信息：stu_info.name  stu_info.age  .....
        for item in self.list_stu:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def add_student(self, stu):
        """
        添加学生对象
        :param: stu   学生对象
        """
        stu.id = len(self.__list_stu) + 1
        self.__list_stu.append(stu)

    def sort_score(self):
        sorted_list = self.__list_stu[:]
        for l in range(len(sorted_list) - 1):
            for r in range(l + 1, len(sorted_list)):
                if sorted_list[l].score < sorted_list[r].score:
                    sorted_list[l], sorted_list[r] = sorted_list[r], sorted_list[l]
        return sorted_list

class StudentManagerView:
    """
    界面控制类, 调用逻辑控制类
    """
    def __init__(self):
        #创建逻辑控制类对象
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("--------------------------------")
        print("1)Add student")
        print("2)Display student")
        print("3)Delete student")
        print("4)Update student")
        print("5)Display student by score")
        print("--------------------------------")

    def __select_menu(self):
        number = input("Please select a choice, type 'y' to exit: ")
        if   number == "1":
            self.__input_student()
        elif number == "2":
            self.__display_student(self.__controller.list_stu)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__update_student(self.__controller.stu_info)
        elif number == "5":
            self.__sort_list()

    def main(self):
        """
        管理器入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        while True:
            stu = StudentModel()
            stu.name  = input("Please input name: ")
            stu.age   = input("Please input age: ")
            stu.score = input("Please input score: ")
            self.__controller.add_student(stu)  #调用逻辑控制类对象
            if input("Please press 'y' to continue: ") != "y":
                break

    def __display_student(self, list_stu):
        """
        显示学生列表
        :param: list_stu   需要显示的列表
        """
        for item in list_stu:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        while True:
            id = int(input("Please input student's ID: "))
            result = self.__controller.remove_student(id)
            if result:
                print("Delete successful!")
            else:
                print("Delete failed")
            if input("Please press 'y' to continue: ") != "y":
                break

    def __update_student(self, stu_info):
        stu_info = StudentModel()
        stu_info.
        self.__controller.update_student()
        pass

    def __sort_list(self):
        self.__controller.sorted_list()
        pass

view = StudentManagerView()
view.main()

#debug
"""
list_stu = [
    StudentModel(101, "zs", 12, 86),
    StudentModel(104, "ww", 13, 90),
    StudentModel(102, "ls", 14, 100),
    StudentModel(103, "ww", 12, 90),
]


manager = StudentManagerController()
stu01 = StudentModel(name="zs",age = 24, score = 100)
stu02 = StudentModel(name="ls",age = 23, score = 86)
stu03 = StudentModel(name="ww",age = 21, score = 97)
stu04 = StudentModel(name="ml",age = 22, score = 80)
manager.add_student(stu01)
manager.add_student(stu02)
manager.add_student(stu03)
manager.add_student(stu04)

result = manager.sort_score()
print(result)

"""

