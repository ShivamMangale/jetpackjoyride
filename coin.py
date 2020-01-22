class coin():
	def __init__(self, screen, x, y):
		self.__x = x
		self.__y = y
		if screen[self.__x][self.__y] != 6:	
			for i in range(3):
				screen[self.__x][self.__y + i] = 99
		