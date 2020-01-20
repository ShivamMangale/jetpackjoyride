class checker:
	invalid = 6
	coin = 99
	looks = [[ord("-"), ord(" "), ord("-")],
				  [ord(" "), ord("."), ord(" ")],
				  [ord("_"), ord(" "), ord("_")]]
				  
	def __init__(self):
		pass

	def enableshield(self, screen, start, x, y, l, b):
		pass

	def disableshield(self, screen, start, x, y, l, b):
		pass

	def dochange(self, screen, x, y, lives, shield, l, b):
		diff = 0
		for i in range(max(x-5,4), min(x+5,l-4)):
			for j in range(max(0,y-5), min(b,y+5)):
				if screen[i][j] == 6:
					screen[i][j] = ord(" ")
					diff = 1
		if shield == 1:	diff = 0
		return lives - diff


	def limit(self, lim, x):
		if x < lim:		return 1
		else:			return 0
	
	def domove(self, screen, move, start, x, y, l, b, score, lives, shield):
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = ord(" ")
		
		if move == 0:
			x -= 2
			x = max(2,x)
		elif move == 1:
			y += 2
		elif move == 2:
			y -= 1
		
		for i in range(x,x+3):
			for j in range(y,y+3):
				if screen[i][j] == self.coin:	score += 1
				elif screen[i][j] == self.invalid:	lives = self.dochange(screen, i, j, lives, shield, l, b)
				screen[i][j] = self.looks[i - x][j - y]

		return x, y, score, lives

	def down(self, screen, start, x, y, l, b, grav, score, lives, shield):
		if self.limit(l-4,x)	== 1:
			if grav == 1:
				for i in range(x,x+3):
					for j in range(y,y+3):
						screen[i][j] = ord(" ")

				x += 1

				for i in range(x,x+3):
					for j in range(y,y+3):
						if screen[i][j] == self.coin:	score += 1
						elif screen[i][j] == self.invalid:	lives = self.dochange(screen, i, j, lives, shield, l, b)
						screen[i][j] = self.looks[i - x][j - y]
			else:
				grav = 1

		return x, y, grav, score, lives
