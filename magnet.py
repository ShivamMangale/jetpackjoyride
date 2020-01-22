class magnet():
	def __init__(self, screen, x, y, obst):
		self.__x = x
		self.__y = y
		for i in range(3):
				screen[self.__x][self.__y + i] = obst[0][i]

	def getmagx(self):
		return self.__x

	def getmagy(self):
		return self.__y