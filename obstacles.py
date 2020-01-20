import random
class obstacles:
	o = []
	o.append([[6, ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), 6, ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), 6, ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), 6]])
	o.append([[ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")]])
	o.append([[ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [6, 6, 6, 6, 6], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")]])
	o.append([[ord("m"), ord("a"), ord("g")]])
	o.append([[ord("S")]])
	def __init__(self, screen, l, b):
		start = 20
		while start < b - 100:
			loc = random.randint(2,l - 7)
			if screen[loc][start] != 6:	
				for i in range(3):
					screen[loc][start + i] = 99
			start = start + random.randint(8,12)
		start = 20
		while start < b - 100:
			obst = self.o[random.randint(0,2)]
			loc = random.randint(2,l - 7)
			for i in range(loc,loc+5):
				for j in range(start,start + 5):
					screen[i][j] = obst[i - loc][j - start]
			start = start + random.randint(20,40)
		start = 20
		
	def speed(self, screen, l, b):
		start = 20
		start = start + random.randint(100,200)
		loc = random.randint(2,l-7)
		screen[loc][start] = self.o[4][0][0]

		return loc, start

	def magnet(self, screen, l, b):	
		start = 20
		start = start + random.randint(100,200)
		loc = random.randint(2,l-7)
		obst = self.o[3]
		for i in range(3):
				screen[loc][start + i] = obst[0][i]

		return loc, start
		