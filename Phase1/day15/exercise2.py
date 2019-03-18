import math

class Graphics:
	def __init__(self, name):
		self.name = name

	def image(self):
		raise NotImplementedError()

class Circle(Graphics):
	def __init__(self, name, radius = 0):
		super().__init__(name)
		self.radius = radius

	def image(self):
		return math.pi * self.radius ** 2

class Rectangle(Graphics):
	def __init__(self, name, length = 0, width = 0):
		super().__init__(name)
		self.length = length
		self.width = width

	def image(self):
		return self.length * self.width

class Triangle(Graphics):
	def __init__(self, name, bottom = 0, high = 0):
		super().__init__(name)
		self.bottom = bottom
		self.high = high
		
	def image(self):
		return self.bottom * self.high / 2

class GraphicsManager:
	def __init__(self):
		self.graphics = []

	def calculate_all(self):
		sum = 0
		for item in self.graphics:
			sum += item.image()
		return sum

c01 = Circle("大圆形",10)
c02 = Circle("小圆形",2)

r01 = Rectangle("大矩形",5,8)
r02 = Rectangle("小矩形",2,3)

manager = GraphicsManager()
manager.graphics.append(c01)
manager.graphics.append(c02)
manager.graphics.append(r01)
manager.graphics.append(r02)

total_area = manager.calculate_all()
print(total_area)