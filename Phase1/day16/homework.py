class Profession:
	def __init__(self, HP, MP, )
	pass

class Shaolin(Profession):
	pass

class Xiaoyao(Profession):
	pass

class Gaibang(Profession):
	pass

class Skill_Deployer:
	"""
		技能释放器
	"""
	def __init__(seflf):
		
		
	def config_skill(self):
		"""
			配置技能，创建技能依赖的影响效果对象
		"""


class Effection(Skill_Deployer):
	"""
		影响效果
	"""
	def impact(self):
		raise NotImplementedError()

class CostSpEffect(Effection):
	"""
		消耗法力
	"""
	def __init__(self, value):
		self.value = value

	def impact(self):
		print("消耗法力"%self.value)

class Damage_skill(Effection):
	"""
		伤害生命
	"""
	def __init__(self, value):
		self.value = value

	def impact(self):
		print("伤害%s生命"%self.value)

class Buff(Effection):
	"""
		Buff
	"""
	def __init__(self, value):
		self.value = value

	def impact(self):
		print("增加%s攻击力"%self.value)

class Debuff(Effection):
	"""
		Debuff
	"""
	def __init__(self, value):
		self.value = value

	def impact(self):
		print("降低%s防御力"%self.value)


# 设计类的时候先找行为，用行为去定义类，属性放最后