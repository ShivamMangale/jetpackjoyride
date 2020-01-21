import random
class obstacles:
	def __init__(self, board, l, b):
		screen = board.getscreen()
		self.__o = []
		self.__o.append([[6, ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), 6, ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), 6, ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), 6]])
		self.__o.append([[ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")]])
		self.__o.append([[ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [6, 6, 6, 6, 6], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")]])
		self.__o.append([[ord("m"), ord("a"), ord("g")]])
		self.__o.append([[ord("S")]])
		start = 20
		while start < b - 100:
			loc = random.randint(2,l - 7)
			if screen[loc][start] != 6:	
				for i in range(3):
					screen[loc][start + i] = 99
			start = start + random.randint(8,12)
		start = 20
		while start < b - 100:
			obst = self.__o[random.randint(0,2)]
			loc = random.randint(2,l - 7)
			for i in range(loc,loc+5):
				for j in range(start,start + 5):
					screen[i][j] = obst[i - loc][j - start]
			start = start + random.randint(20,40)
		start = 20
		board.setscreen(screen)
		
	def speed(self, board, l, b):
		screen = board.getscreen()
		start = 20
		start = start + random.randint(100,200)
		loc = random.randint(2,l-7)
		screen[loc][start] = self.__o[4][0][0]

		return loc, start
		board.setscreen(screen)

	def magnet(self, board, l, b):	
		screen = board.getscreen()
		start = 20
		start = start + random.randint(100,200)
		loc = random.randint(2,l-7)
		obst = self.__o[3]
		for i in range(3):
				screen[loc][start + i] = obst[0][i]

		return loc, start
		board.setscreen(screen)
