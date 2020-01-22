from person import person
import time

class mando(person):
	def __init__(self, board, x, y):
		super().__init__(x,y,10)
		screen = board.getscreen()
		self.__looks = [["#", "T", "#"],
					  	["|", "|", ">"],
					  	["/", "|", "\\"]]
		self.__score = 0
		self.__invalid = "!"
		self.__coin = "$"
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.__looks[i - x][j - y]
		self.__speedup = 1
		self.__speedinit = time.time() + 1000
		self.__bullets = []
		self.__flagshield = -1
		self.__timeofshield = time.time() + 10000
		self.__shieldable = 0
		self.__timeofshieldend = -1
		self.__grav = 0
		board.setscreen(screen)

	def isspeed(self, x, y):
		if self.__speedup == 1:
			if x == self._x or x == self._x + 1 or x == self._x + 2:
				if y == self._y or y == self._y + 1 or y == self._y + 2:
					self.__speedup = 5
					self.__speedinit = time.time()
		elif self.__speedup == 5:
			if time.time() - self.__speedinit > 17:
				self.__speedup = 1

	def shoot(self):
		self.__bullets.append([self._x + 1, self._y + 3])

	def updatebullets(self, en, screen, start, l, b):
		hurt = 0
		for i in range(self.__speedup):	
			for shots in self.__bullets:
				if shots[1] < b-3:
					if screen[shots[0]][shots[1] + 1] == "!" or screen[shots[0]][shots[1] + 2] == "!" or screen[shots[0]][shots[1] + 3] == "!":
						for i in range(max(2,shots[0]-7),min(l-2,shots[0]+7)):
							for j in range(max(start,shots[1]-7),min(min(start+100,shots[1]+7),b)):
								if screen[i][j] == "!":
									screen[i][j] = " "
						self.__score += 10
						screen[shots[0]][shots[1]] = " "
						shots[0],shots[1] = b + 100, b + 100
					elif screen[shots[0]][shots[1] + 1] == "$" or screen[shots[0]][shots[1] + 2] == "$" or screen[shots[0]][shots[1] + 3] == "$":
						screen[shots[0]][shots[1]] = " "
						self.__score += 3
						for i in range(shots[1] + 1,shots[1] + 4):
							if screen[shots[0]][i] == "$":
								for j in range(i,i+3):
									screen[shots[0]][j] = " "
						shots[0],shots[1] = b + 100, b + 100
					# elif screen[shots[0]][shots[1] + 1] == "+" or screen[shots[0]][shots[1] + 2] == "+" or screen[shots[0]][shots[1] + 3] == "+" or screen[shots[0]][shots[1] + 1] == "[" or screen[shots[0]][shots[1] + 2] == "[" or screen[shots[0]][shots[1] + 3] == "[" :
					# 	hurt += 1
					# 	screen[shots[0]][shots[1]] = " "
					# 	shots[0], shots[1] = b + 100,b + 100
					elif screen[shots[0]][shots[1] + 1] == "S" or screen[shots[0]][shots[1] + 2] == "S" or screen[shots[0]][shots[1] + 3] == "S":
						for i in range(3):
							if screen[shots[0]][shots[1] + i + 1] == "S":
								self.isspeed(self._x, self._y)
								screen[shots[0]][shots[1] + i + 1] = " "
						screen[shots[0]][shots[1]] = " "						
						shots[0], shots[1] = b + 100,b + 100
					elif screen[shots[0]][shots[1] + 1] == " " or screen[shots[0]][shots[1] + 2] == " " or screen[shots[0]][shots[1] + 3] == " ":
						screen[shots[0]][shots[1]] = " "
						screen[shots[0]][shots[1] + 1] = " "
						screen[shots[0]][shots[1] + 2] = " "
						screen[shots[0]][shots[1] + 3] = "@"
						shots[1] = shots[1] + 3
						if shots[1] > start + 100:	
							screen[shots[0]][shots[1]] = " "
							shots[0], shots[1] = b + 100,b + 100
					else:
						hurt += 1
						screen[shots[0]][shots[1]] = " "
						shots[0], shots[1] = b + 100,b + 100
				elif shots[1] != b + 100:
					screen[shots[0]][shots[1]] = " "
					shots[0], shots[1] = b + 100,b + 100

		en.setlives(en.getlives() - hurt)

	def tryshield(self):
		if self.__flagshield == -1 and self.__shieldable == 1:
			self.__flagshield = 1
			self.__timeofshield = time.time() 
		
	def updateshield(self):	
		if self.__flagshield == 1 and time.time() - self.__timeofshield > 10:	
			self.__flagshield = -1
			self.__timeofshieldend = time.time()
			self.__shieldable = 0
		elif time.time() - self.__timeofshieldend > 60:
			self.__shieldable = 1

	def dochange(self, screen, x, y, l, b):
		diff = 0
		for i in range(max(x-6,4), min(x+6,l-4)):
			for j in range(max(0,y-7), min(b,y+7)):
				if screen[i][j] == "!":
					screen[i][j] = " "
					diff = 1
		if self.__flagshield == 1:	diff = 0
		self._lives -= diff

	def domove(self, screen, move, start, l, b, en):
		for i in range(self._x, self._x + 3):
			for j in range(self._y, self._y + 3):
				screen[i][j] = " "
		
		if move == 0:
			self._x -= 2
			self._x = max(3,self._x)
		elif move == 1:
			self._y += 2
			self._y = min(start + 100 - 4,self._y)
			if self._y >= en.gety() - 1:
				self._y = en.gety() - 4
		elif move == 2:
			self._y -= 2
		
		for i in range(self._x,self._x+3):
			for j in range(self._y,self._y+3):
				if screen[i][j] == self.__coin:	self.__score += 1
				elif screen[i][j] == self.__invalid:	self.dochange(screen, i, j, l, b)
				screen[i][j] = self.__looks[i - self._x][j - self._y]

	def limit(self, lim, x):
		if x < lim:		return 1
		else:			return 0
	
	def down(self, screen, start, l, b):
		if self.limit(l-4,self._x)	== 1:
			if self.__grav:
				for i in range(self._x,self._x+3):
					for j in range(self._y,self._y+3):
						screen[i][j] = " "

				self._x += int(self.__grav/2)
				self.__grav += 1
				self._x = min(self._x, l-4)

				for i in range(self._x,self._x+3):
					for j in range(self._y,self._y+3):
						if screen[i][j] == self.__coin:	self.__score += 1
						elif screen[i][j] == self.__invalid:	self.dochange(screen, i, j, l, b)
						screen[i][j] = self.__looks[i - self._x][j - self._y]
			else:
				self.__grav = 1

		return self.__grav

	def gravity(self, screen, start, l, b, move):	
		if move != 'w':	
			self.__grav = self.down(screen, start, l, b)
			if not self.__grav and self._x == l-4:	
				self.__grav = 0
		elif move == 'w' and self.__grav:
			self.__grav = 0

	def getflagshield(self):
		return self.__flagshield

	def getscore(self):
		return self.__score

	def setscore(self, upd):
		self.__score = upd

	def getspeedup(self):
		return self.__speedup

	def checkmagnet(self, screen, start, l, b, movemap, magx, magy, en):
		if start <= magy and magy < start + 100:
			mag = ['m', 'a', 'g']
			for i in range(3):
				screen[magx][magy + i + 1] = " "
				screen[magx][magy + i] = mag[i]
			if self.gety() <= magy:
				self.domove(screen, movemap['d'], start, l, b, en)
			else:
				self.domove(screen, movemap['a'], start, l, b, en)
	
	def setscore(self,upd):
		self.__score += upd