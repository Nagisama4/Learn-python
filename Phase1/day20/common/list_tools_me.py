"""
    对列表常用操作的模块
"""
class ListHelper:
    """
        列表助手类:定义对列表的通用操作
    """
    @staticmethod
    def find_all(list_target, func_condition):
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(list_target,func_condition):
        for item in list_target:
            # if item.age < 30:
            if func_condition(item):
                return item

    @staticmethod
    def count(list_target,func_condition):
        int_count = 0
        for item in list_target:
            if func_condition(item):
                int_count += 1
        return int_count

    @staticmethod
    def find_max(list_target, func_condition):
        smax = list_target[0]
        for item in range(1, len(list_target)):
            if func_condition(smax) < func_condition(list_target[item]):
                smax = list_target[item]
        return smax

    @staticmethod
    def find_min(list_target, func_condition):
        pass

    @staticmethod
    def allsum(list_target, func_condition):
        ssum = 0
        for item in list_target:
            ssum += func_condition(item)
        return ssum

    @staticmethod
    def obtain_element(list_target, func_condition):
        for item in list_target:
            yield func_condition(item)


    @staticmethod
    def high_sort(list_target, func_condition):
        for left in range(len(list_target) - 1):
            for right in range(left + 1, len(list_target)):
                if func_condition(list_target[left]) > func_condition(list_target[right]):
                    list_target[left], list_target[right] = list_target[right], list_target[left]
        return list_target

    @staticmethod
    def low_sort(list_target, func_condition):
        for left in range(len(list_target) - 1):
            for right in range(left + 1, len(list_target)):
                if func_condition(list_target[left]) < func_condition(list_target[right]):
                    list_target[left], list_target[right] = list_target[right], list_target[left]
        return list_target