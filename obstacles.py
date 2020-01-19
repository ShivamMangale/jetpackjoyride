import random
#can change obstacle values such that 6,7,8 showing each different type or even have it such that 61,62,63,64,65 so as to be able to also find the part of the obstacle with the type
class obstacles:
	o = []
	o.append([[6, ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), 6, ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), 6, ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), 6]])
	o.append([[ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")]])
	o.append([[ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [6, 6, 6, 6, 6], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")]])
	o.append([[ord("|"), ord("|")], [ord("|"), ord("|")]])
	def __init__(self, screen, l, b):
		start = 20
		while start < b - 10:
			loc = random.randint(2,l - 7)
			if screen[loc][start] != 6:	
				for i in range(3):
					screen[loc][start + i] = 99
			start = start + random.randint(8,12)
		start = 20
		while start < b - 10:
			obst = self.o[random.randint(0,2)]
			loc = random.randint(2,l - 7)
			for i in range(loc,loc+5):
				for j in range(start,start + 5):
					screen[i][j] = obst[i - loc][j - start]
			start = start + random.randint(20,40)
	
	def magnet(self, screen, l, b):	
		start = 20
		start = start + random.randint(100,200)
		loc = random.randint(2,l-7)
		obst = self.o[3]
		for i in range(2):
			for j in range(2):
				screen[loc + i][start + j] = obst[i][j]

		return loc, start