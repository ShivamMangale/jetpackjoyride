import random
#can change obstacle values such that 6,7,8 showing each different type or even have it such that 61,62,63,64,65 so as to be able to also find the part of the obstacle with the type
class obstacles:
	o = []
	o.append([[6, ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), 6, ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), 6, ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), 6]])
	o.append([[ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")], [ord(" "), ord(" "), 6, ord(" "), ord(" ")]])
	o.append([[ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [6, 6, 6, 6, 6], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")], [ord(" "), ord(" "), ord(" "), ord(" "), ord(" ")]])
	def __init__(self, screen, l, b):
		start = 20
		while start < b - 10:
			obst = self.o[random.randint(0,2)]
			loc = random.randint(2,l - 7)
			for i in range(loc,loc+5):
				for j in range(start,start + 5):
					screen[i][j] = obst[i - loc][j - start]
			start = start + random.randint(20,40)
		start = 20
		while start < b - 10:
			loc = random.randint(2,l - 7)
			if screen[loc][start] != 6:	screen[loc][start] = 99
			start = start + random.randint(1,7)