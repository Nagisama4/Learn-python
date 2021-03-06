"""
    day15 复习
    面向对象三大特征
    1. 封装
        分而治之  封装变化  高内聚   低耦合
        class 类:
            def __init__(self):
                self.数据1 = ...
                self.数据2 = ...
                self.数据3 = ...

            def 功能():
                实现细节

        变量 = 构造函数(参数)
        变量.功能()


    2. 继承
        重用现有类的功能与概念，并在此基础上进行扩展。
        class 类名(父类1,父类2....):
            def __init__(self,父类参数,自身参数):
                super().__init__(父类参数)
                self.变量 = 自身参数


    3. 多态
        调用父类的一个方法，在不同的子类对象中，有不同的实现效果。
        def 回家(交通工具):
            交通工具.运输()

        回家(火车)
        回家(汽车)

        def 统计所有图形面积():
            sum = 0
            for item in 所有图形:
                sum += item.计算面积()
            return sum

        所有图形.添加图形(圆形)
        所有图形.添加图形(矩形)
        统计所有图形面积()

        本质：
        调用：
            父类.方法()
        实际：
            子类1.方法()
            子类2.方法()
"""













