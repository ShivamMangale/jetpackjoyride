from person import person
import time

class enemy(person):
	def __init__(self, screen, x, y, timeofstart):
		super().__init__(x,y,5)
		self.looks = [[ord("+"), ord(":"), ord("+")],
					  [ord("["), ord(":"), ord("]")],
					  [ord("["), ord(":"), ord("]")]]
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.looks[i-x][j-y]
		self.enemybullet = []
		self.reachedenemy = -1
		self.timeforenemybullet = timeofstart + 100000

	def move(self, screen, x, b):
		b -= 4
		while self.x != x:
			for i in range(self.x,self.x+3):
				for j in range(b,b+3):
					screen[i][j] = ord(" ")
			if self.x < x:		self.x += 1
			else:			self.x -= 1

			for i in range(self.x,self.x+3):
				for j in range(b,b+3):
					screen[i][j] = self.looks[i - self.x][j - b]

		return self.x

	def enemyreached(self):
		if self.reachedenemy == -1:
			self.reachedenemy = 1
			self.timeforenemybullet = time.time()

	def checkifenemyshoot(self):
		if time.time() - self.timeforenemybullet > 1:
			for i in range(1):
				self.enemybullet.append([self.x + i, self.y - 1])
			self.timeforenemybullet = time.time()

	def updatebullets(self, screen, x, y, shield):
		hurt = 0
		for i in self.enemybullet:
			if i[1] > 900:
				if x <= i[0] and x + 3 > i[0]:
					if y <= i[1] and y + 3 > i[1]:
						if shield == -1:
							hurt += 1
						screen[i[0]][i[1]] = ord(" ")
						i[0], i[1] = 0, 0
				screen[i[0]][i[1]] = ord(" ")
				i[1] -= 3
				screen[i[0]][i[1]] = ord("e")
			else:
				i[0], i[1] = 20, 100

		return hurt
