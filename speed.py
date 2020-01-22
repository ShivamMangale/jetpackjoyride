class speed:
	def __init__(self, screen, x, y, obst):
		self.__x = x
		self.__y = y
		screen[x][y] = obst
