class beam():
	def __init__(self, screen, x, y, obst):
		self.__x = x
		self.__y = y
		self.__type = obst

		for i in range(self.__x,self.__x+5):
			for j in range(self.__y,self.__y + 5):
				screen[i][j] = self.__type[i - self.__x][j - self.__y]
			
		if screen[self.__x][self.__y] != 6:	
			for i in range(3):
				screen[self.__x][self.__y + i] = 99
		