class Pet:
	def　__init__(self, name):
		self.name = name

class Dog(Pet):
	def __init__(self, name, job):
		self.job = job
		super().__init__(name)

class Cat(Pet):
	def __init__(self, name, claw):
		self.claw = claw
		super().__init__(name)