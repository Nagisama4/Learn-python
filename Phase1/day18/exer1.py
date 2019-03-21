class ScoreError:
	def __init__(self, wrong, msg):
		self.wrong = wrong
		self.msg = msg

class Student:
	def __init__(self,score):
		self.score = score

	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if 0 <= score <= 100:
			self.__score = value
		else:
			raise ScoreError()

def getscore():
	while True:
		score = int(input("请输入分数(0-100)："))	
		if 0 <= score <= 100:
			print("分数为：%d" % score)
			break
		else:
			print("输入范围错误")


try:
	getscore()
except ScoreError as e:
	print("输入有误")
	getscore()