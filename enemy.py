from person import person

class enemy(person):
	def __init__(self, screen, x, y):
		super().__init__(x,y,5)
		self.looks = [[ord("+"), ord(":"), ord("+")],
					  [ord("["), ord(":"), ord("]")],
					  [ord("["), ord(":"), ord("]")]]
		for i in range(x,x+3):
			for j in range(y,y+3):
				screen[i][j] = self.looks[i-x][j-y]


	def move(self, screen, start, cur, x, l, b):
		b -= 4
		while cur != x:
			for i in range(cur,cur+3):
				for j in range(b,b+3):
					screen[i][j] = ord(" ")
			if cur < x:		cur += 1
			else:			cur -= 1

			for i in range(cur,cur+3):
				for j in range(b,b+3):
					screen[i][j] = self.looks[i - cur][j - b]

		return cur