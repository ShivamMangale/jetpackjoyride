from person import person
import time

class mando(person):
	invalid = 6
	coin = 99
	def __init__(self,screen,x,y):
		super().__init__(x,y,10)
		self.looks = [[ord("-"), ord(" "), ord("-")],
					  [ord(" "), ord("."), ord(" ")],
					  [ord("_"), ord(" "), ord("_")]]
		self.score = 0
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.looks[i - x][j - y]
		self.speedup = 1
		self.speedinit = time.time() + 1000
		self.bullets = []
		self.flagshield = -1
		self.timeofshield = time.time() + 10000
		self.shieldable = 0
		self.timeofshieldend = -1
		self.grav = 0

	def isspeed(self, x, y):
		if self.speedup == 1:
			if x == self.x or x == self.x + 1 or x == self.x + 2:
				if y == self.y or y == self.y + 1 or y == self.y + 2:
					self.speedup = 5
					self.speedinit = time.time()
		elif self.speedup == 5:
			if time.time() - self.speedinit > 17:
				self.speedup = 1

	def shoot(self):
		self.bullets.append([self.x + 1, self.y + 3])

	def updatebullets(self, screen, start, l, b):
		hurt = 0
		for i in range(self.speedup):	
			for shots in self.bullets:
				if shots[1] < b-3:
					if screen[shots[0]][shots[1] + 1] == 6 or screen[shots[0]][shots[1] + 2] == 6 or screen[shots[0]][shots[1] + 3] == 6:
						for i in range(max(2,shots[0]-7),min(l-2,shots[0]+7)):
							for j in range(max(start,shots[1]-7),min(min(start+100,shots[1]+7),b)):
								if screen[i][j] == 6:
									screen[i][j] = ord(" ")
						screen[shots[0]][shots[1]] = ord(" ")
						shots[0],shots[1] = b + 100, b + 100
					elif screen[shots[0]][shots[1] + 1] == 99 or screen[shots[0]][shots[1] + 2] == 99 or screen[shots[0]][shots[1] + 3] == 99:
						screen[shots[0]][shots[1]] = ord(" ")
						self.score += 1
						for i in range(shots[1] + 1,shots[1] + 4):
							if screen[shots[0]][i] == 99:
								for j in range(i,i+3):
									screen[shots[0]][j] = ord(" ")
						shots[0],shots[1] = b + 100, b + 100
					elif screen[shots[0]][shots[1] + 1] == ord("+") or screen[shots[0]][shots[1] + 2] == ord("+") or screen[shots[0]][shots[1] + 3] == ord("+") or screen[shots[0]][shots[1] + 1] == ord("[") or screen[shots[0]][shots[1] + 2] == ord("[") or screen[shots[0]][shots[1] + 3] == ord("["):
						hurt += 1
						screen[shots[0]][shots[1]] = ord(" ")
						shots[0], shots[1] = b + 100,b + 100
					else:
						screen[shots[0]][shots[1]] = ord(" ")
						screen[shots[0]][shots[1] + 1] = ord(" ")
						screen[shots[0]][shots[1] + 2] = ord(" ")
						screen[shots[0]][shots[1] + 3] = ord("@")
						shots[1] = shots[1] + 3
						if shots[1] > start + 100:	
							screen[shots[0]][shots[1]] = ord(" ")
							shots[0], shots[1] = b + 100,b + 100
				elif shots[1] != b + 100:
					screen[shots[0]][shots[1]] = ord(" ")
					shots[0], shots[1] = b + 100,b + 100

		return hurt

	def tryshield(self):
		if self.flagshield == -1 and self.shieldable == 1:
			self.flagshield = 1
			self.timeofshield = time.time() 
		
		return self.flagshield

	def updateshield(self):	
		if self.flagshield == 1 and time.time() - self.timeofshield > 10:	
			self.flagshield = -1
			self.timeofshieldend = time.time()
			self.shieldable = 0
		elif time.time() - self.timeofshieldend > 10:
			self.shieldable = 1

		return self.flagshield

	def dochange(self, screen, x, y, l, b):
		diff = 0
		for i in range(max(x-6,4), min(x+6,l-4)):
			for j in range(max(0,y-7), min(b,y+7)):
				if screen[i][j] == 6:
					screen[i][j] = ord(" ")
					diff = 1
		if self.flagshield == 1:	diff = 0
		self.lives -= diff

	def domove(self, screen, move, start, l, b):
		for i in range(self.x,self.x+3):
			for j in range(self.y,self.y+3):
				screen[i][j] = ord(" ")
		
		if move == 0:
			self.x -= 2
			self.x = max(2,self.x)
		elif move == 1:
			self.y += 2
			self.y = min(start + 100 - 4,self.y)
		elif move == 2:
			self.y -= 2
		
		for i in range(self.x,self.x+3):
			for j in range(self.y,self.y+3):
				if screen[i][j] == self.coin:	self.score += 1
				elif screen[i][j] == self.invalid:	self.dochange(screen, i, j, l, b)
				screen[i][j] = self.looks[i - self.x][j - self.y]

	def limit(self, lim, x):
		if x < lim:		return 1
		else:			return 0
	
	def down(self, screen, start, l, b):
		if self.limit(l-4,self.x)	== 1:
			if self.grav == 1:
				for i in range(self.x,self.x+3):
					for j in range(self.y,self.y+3):
						screen[i][j] = ord(" ")

				self.x += 1

				for i in range(self.x,self.x+3):
					for j in range(self.y,self.y+3):
						if screen[i][j] == self.coin:	self.score += 1
						elif screen[i][j] == self.invalid:	self.dochange(screen, i, j, l, b)
						screen[i][j] = self.looks[i - self.x][j - self.y]
			else:
				self.grav = 1

		return self.grav

	def gravity(self, screen, start, l, b, move):	
		if move != 'w':	
			self.grav = self.down(screen, start, l, b)
			if self.grav == 1 and self.x == l-4:	
				self.grav = 0
		elif move == 'w' and self.grav == 1:
			self.grav = 0

