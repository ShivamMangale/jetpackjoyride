class person:
	def __init__(self, x, y, lives):
		self._x = x
		self._y = y
		self._lives = lives

	def getx(self):
		return self._x

	def gety(self):
		return self._y

	def getlives(self):
		return self._lives

	def setlives(self, upd):
		self._lives = upd