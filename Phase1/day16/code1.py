class Employee:
    def __init__(self,name, job_object):
        self.name = name
        self.job_object = job_object


    def get_salary(self):
        return self.job_object.calculate_salary()

class Job:
    def __init__(self,base_salary):
        self.base_salary = base_salary


    def calculate_salary(self):
        return self.base_salary


class Programmer(Job):
    def __init__(self,base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return super().base_salary + self.bonus
        return super().calculate_salary() + self.bonus

class Tester(Job):
    def __init__(self,base_salary,bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5

class Salesmen(Job):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return super().calculate_salary() + self.sale_value * 0.05

