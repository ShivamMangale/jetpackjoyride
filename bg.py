import numpy

class bg:
	sky = '\033[94m^\033[0m'
	skytil = '\033[94m~\033[0m'
	ground = '\033[32m*\033[0m'
	coin = '\033[01m\033[93m$\033[0m'
	danger = '\033[01m\033[41m\033[30m!\033[0m'
	blueforshield = '\033[44m'
	herobullet = '\033[96m@\033[0m'
	enemybullet = '\033[33me\033[0m'
	mmag = '\033[40m\033[31mm\033[0m'
	amag = '\033[40m\033[31ma\033[0m'
	gmag = '\033[40m\033[31mg\033[0m'
	def __init__(self,rows,cols):
		self.__rows = rows + 2
		self.__cols = cols
		self.screen = numpy.full((rows + 2,cols),' ')
		for i in range(self.__cols):
			self.screen[0][i] = '^'
			self.screen[1][i] = "~"
			self.screen[2][i] = '^'
			self.screen[self.__rows - 3][i] = '*'
			self.screen[self.__rows - 2][i] = '*'
			self.screen[self.__rows - 1][i] = '*'


	def printall(self):
		for i in range(self.__rows):
			for j in range(self.__cols):
				if self.screen[i][j] == " ":
					print(' ',end='')
				elif self.screen[i][j] == '^':
					print(self.sky,end='')
				elif self.screen[i][j] == "~":
					print(self.skytil,end='')
				elif self.screen[i][j] == '*':
					print(self.ground,end='')
				elif self.screen[i][j] == " ":
					print(" ",end='')
				elif self.screen[i][j] == "-":
					print("-",end='')
				elif self.screen[i][j] == "_":
					print("_",end='')
				elif self.screen[i][j] == "o":
					print("o",end='')
				elif self.screen[i][j] == "[":
					print("[",end='')
				elif self.screen[i][j] == ":":
					print(":",end='')
				elif self.screen[i][j] == "]":
					print("]",end='')
				elif self.screen[i][j] == "+":
					print("+",end='')
				elif self.screen[i][j] == "|":
					print("|",end='')
				elif self.screen[i][j] == "@":
					print(self.herobullet,end='')
				elif self.screen[i][j] == "e":
					print(self.enemybullet,end='')
				elif self.screen[i][j] == "S":
					print("\033[34mS\033[0m",end='')
				elif self.screen[i][j] == "!":
					print(self.danger,end='')
				elif self.screen[i][j] == "$":
					print(self.coin,end='')			
			print()
			
	def printonly(self,start,shield):
		for i in range(self.__rows):
			for j in range(start,min(start+100,self.__cols)):
				if self.screen[i][j] == 0:
					print(' ',end='')
				elif self.screen[i][j] == '^':
					print(self.sky,end='')
				elif self.screen[i][j] == "~":
					print(self.skytil,end='')
				elif self.screen[i][j] == '*':
					print(self.ground,end='')
				elif self.screen[i][j] == " ":
					print(" ",end='')
				elif shield == -1 and self.screen[i][j] == "#":
					print("\033[40m\033[93m#\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == "|":
					print("\033[40m\033[93m|\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == ">":
					print("\033[40m\033[93m>\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == "\\":
					print("\033[40m\033[93m\\\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == "/":
					print("\033[40m\033[93m/\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == "T":
					print("\033[40m\033[93mT\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == "#":
					print("\033[44m#\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == "|":
					print("\033[44m\033[93m|\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == ">":
					print("\033[44m\033[93m>\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == "/":
					print("\033[44m\033[93m/\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == "T":
					print("\033[44m\033[93mT\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == "\\":
					print("\033[44m\033[93m\\\033[0m",end='')
				elif self.screen[i][j] == "[":
					print("[",end='')
				elif self.screen[i][j] == ":":
					print(":",end='')
				elif self.screen[i][j] == "]":
					print("]",end='')
				elif self.screen[i][j] == "+":
					print("+",end='')
				elif self.screen[i][j] == "|":
					print("|",end='')
				elif self.screen[i][j] == "@":
					print(self.herobullet,end='')
				elif self.screen[i][j] == "e":
					print(self.enemybullet,end='')
				elif self.screen[i][j] == "m":
					print(self.mmag,end='')
				elif self.screen[i][j] == "a":
					print(self.amag,end='')
				elif self.screen[i][j] == "g":
					print(self.gmag,end='')
				elif self.screen[i][j] == "S":
					print("\033[34mS\033[0m",end='')
				elif self.screen[i][j] == "!":
					print(self.danger,end='')
				elif self.screen[i][j] == "$":
					print(self.coin,end='')	
			print()
	
	def getscreen(self):
		return self.screen

	def setscreen(self, upd):
		self.screen = upd