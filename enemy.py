from person import person
from mando import mando
from dragon import dragon
import time

class enemy(person):
	def __init__(self, board, x, y, timeofstart):
		super().__init__(x,y,5)
		screen = board.getscreen()
		self.__image = dragon().looks
		self.__max = 0
		self.__looks = self.__image.split("\n")
		for i in range(len(self.__looks)):
			self.__max = max(self.__max, len(self.__looks))
		for i in range(len(self.__looks)):
			for j in range(self.__max):
				screen[x + i][y + j] = self.__looks[i][j]
		self.__enemybullet = []
		self.__reachedenemy = -1
		self.__timeforenemybullet = timeofstart + 100000
		board.setscreen(screen)

	def move(self, board, x, l, b):
		screen = board.getscreen()
		b -= 4
		for i in range(len(self.__looks)):
			for j in range(self.__max + 6):
				screen[self._x + i][self._y + j] = " "
		self._x = x
		self._x = min(self._x, l - 10)
		for i in range(len(self.__looks)):
			for j in range(self.__max + 6):
				screen[self._x + i][self._y + j] = self.__looks[i][j]
	
		return self._x
		board.setscreen(screen)

	def enemyreached(self):
		if self.__reachedenemy == -1:
			self.__reachedenemy = 1
			self.__timeforenemybullet = time.time()

	def checkifenemyshoot(self):
		if time.time() - self.__timeforenemybullet > 1:
			for i in range(len(self.__looks)):
				self.__enemybullet.append([self._x + i, self._y - 1])
				i += 1
			self.__timeforenemybullet = time.time()

	def updatebullets(self, hero, board):
		screen = board.getscreen()
		hurt = 0
		for i in self.__enemybullet:
			if i[1] > 900:
				if hero.getx() <= i[0] and hero.getx() + 3 > i[0]:
					if hero.gety() <= i[1] and hero.gety() + 3 > i[1]:
						if hero.getflagshield() == -1:
							hurt += 1
						screen[i[0]][i[1]] = " "
						i[0], i[1] = 0, 0
				screen[i[0]][i[1]] = " "
				i[1] -= 3
				screen[i[0]][i[1]] = "e"
			else:
				i[0], i[1] = 20, 100

		hero.setlives(hero.getlives() - hurt)
		board.setscreen(screen)
