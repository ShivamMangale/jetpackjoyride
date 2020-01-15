class checker:
	invalid = [11,12,13]
	coin = 99
	looks = [[ord("-"), ord(" "), ord("-")],
				  [ord(" "), ord("."), ord(" ")],
				  [ord("_"), ord(" "), ord("_")]]

	def __init__(self):
		pass

	def collision(self, start, screen, x, y, move, l, b):
		'''0===up
		   1===right
		   2===left'''
		if move == 0:
			if x == l + 2:	return 2
			elif (screen[x-1][y] in self.invalid) or (screen[x-1][y+1] in self.invalid) or (screen[x-1][y+2] in self.invalid):	return -1
			elif (screen[x-1][y] == self.coin) or (screen[x-1][y+1] == self.coin) or (screen[x-1][y+2] == self.coin):	return 0
			else:		return 1
		elif move == 1:
			if y > (start + b) - 2:	return 10
			elif (screen[x][y+3] in self.invalid) or (screen[x+1][y+3] in self.invalid) or (screen[x+2][y+3] in self.invalid):	return -1
			elif (screen[x][y+3] == self.coin) or (screen[x+1][y+3] == self.coin) or (screen[x+2][y+3] == self.coin):	return 0
			else:		return 1
		elif move == 2:
			if y == start: return 2
			elif (screen[x][y-1] in self.invalid) or (screen[x+1][y-1] in self.invalid) or (screen[x+2][y-1] in self.invalid):	return -1 
			elif (screen[x][y-1] == self.coin) or (screen[x+1][y-1] == self.coin) or (screen[x+2][y-1] == self.coin):	return 0
			else:		return 1
		else:	return 1

	def limit(self, lim, x):
		pass
	
	def domove(self, screen, move, start, x, y, l, b):
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = ord(" ")
		
		if move == 0:
			x -= 1
		elif move == 1:
			y += 1
		elif move == 2:
			y -= 1
		
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.looks[i - x][j - y]

		return x, y
