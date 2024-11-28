class Calculator:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.memory = 0
		self.history = []

	def Add (self,a,b):
		result = a + b
		self.history.append(result)
		return result

	def Mul (self,a,b):
		result = a * b
		self.history.append(result)
		return result

	def Div (self,a,b):
		result = a/b
		self.history.append(result)
		return result

	def Minus (self,a,b):
		result = a - b
		self.history.append(result)
		return result

	def Mod (self,a,b):
		result = a % b
		self.history.append(result)
		return result

	def MemorySave (self, result):
		self.memory = result

	def MemoryAdd (self, result):
		self.memory += result

	def MemorySub (self, result):
		self.memory -= result

	def MemoryClear (self, result):
		self.memory = 0

	def MemoryRead (self):
		return self.memory

	def GetHistory(self):
		for operations in self.history:
			print (operations)