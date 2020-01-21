from person import person
from mando import mando
import time

class enemy(person):
	def __init__(self, board, x, y, timeofstart):
		super().__init__(x,y,5)
		screen = board.getscreen()
		self.__looks = [[ord("+"), ord(":"), ord("+")],
					  [ord("["), ord(":"), ord("]")],
					  [ord("["), ord(":"), ord("]")]]
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.__looks[i-x][j-y]
		self.__enemybullet = []
		self.__reachedenemy = -1
		self.__timeforenemybullet = timeofstart + 100000
		board.setscreen(screen)

	def move(self, board, x, b):
		screen = board.getscreen()
		b -= 4
		while self._x != x:
			for i in range(self._x,self._x+3):
				for j in range(b,b+3):
					screen[i][j] = ord(" ")
			if self._x < x:		self._x += 1
			else:			self._x -= 1

			for i in range(self._x,self._x+3):
				for j in range(b,b+3):
					screen[i][j] = self.__looks[i - self._x][j - b]

		return self._x
		board.setscreen(screen)

	def enemyreached(self):
		if self.__reachedenemy == -1:
			self.__reachedenemy = 1
			self.__timeforenemybullet = time.time()

	def checkifenemyshoot(self):
		if time.time() - self.__timeforenemybullet > 1:
			for i in range(3):
				self.__enemybullet.append([self._x + i, self._y - 1])
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
						screen[i[0]][i[1]] = ord(" ")
						i[0], i[1] = 0, 0
				screen[i[0]][i[1]] = ord(" ")
				i[1] -= 3
				screen[i[0]][i[1]] = ord("e")
			else:
				i[0], i[1] = 20, 100

		hero.setlives(hero.getlives() - hurt)
		board.setscreen(screen)
