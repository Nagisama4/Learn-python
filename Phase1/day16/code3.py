class Vector:
	def __init__(self, x):
		self.x = x

	def __sub__(self, rhs):
		return Vector(self.x - rhs)

	def __mul__(self, rha):
		return Vector(self.x * rha)

	def __isub__(self, rhs):
		self.x -= rhs
		return self

	def __imul__(self, rhs):
		self.x *= rhs
		return self

v01 = Vector(2)
print(id(v01))
v01 -= 4
print(id(v01))
print(v01)