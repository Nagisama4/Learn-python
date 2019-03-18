import math

class Company:
	def __init__(self, name):
		self.name = name

	def salary(self):
		raise NotImplementedError()

class Programmer(Company):
	def __init__(self, name, basement = 0, profit = 0):
		super().__init__(name)
		self.basement = basement
		self.profit = profit

	def salary(self):
		return self.basement + self.profit

class Program_test(Company):
	def __init__(self, name, basement2 = 0, bugs = 0):
		super().__init__(name)
		self.basement2 = basement2
		self.bugs = bugs

	def salary(self):
		return self.basement2 + self.bugs * 5

class Sales(Company):
	def __init__(self, name, basement3 = 0, sales_value = 0):
		super().__init__(name)
		self.basement3 = basement3
		self.sales_value = sales_value
		
	def salary(self):
		return self.basement3 + self.sales_value * 0.05

class CompanyManager:
	def __init__(self):
		self.employees = []

	def calculate_all(self):
		sum = 0
		for item in self.employees:
			sum += item.salary()
		return sum

p01 = Programmer("全栈", 15000, 5000)
p02 = Programmer("算法", 18000, 7000)

pt01 = Program_test("前端", 5000, 30)
pt02 = Program_test("后端", 6000, 50)

s01 = Sales("销售代表", 3000, 20000)
s02 = Sales("分销", 2000, 15000)

manager = CompanyManager()
manager.employees.append(p01)
manager.employees.append(p02)
manager.employees.append(pt01)
manager.employees.append(pt02)
manager.employees.append(s01)
manager.employees.append(s02)

total_salary = manager.calculate_all()
print(total_salary)