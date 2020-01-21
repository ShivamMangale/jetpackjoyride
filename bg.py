import numpy

class bg:
	sky = '\033[94m^\033[0m'
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
		self.__rows = rows
		self.__cols = cols
		self.screen = numpy.zeros(shape=(rows,cols))
		for i in range(self.__cols):
			self.screen[0][i] = -1
			self.screen[self.__rows - 1][i] = -2

	def printall(self):
		for i in range(self.__rows):
			for j in range(self.__cols):
				if self.screen[i][j] == 0:
					print(' ',end='')
				elif self.screen[i][j] == -1:
					print(self.sky,end='')
					# print(j%10,end='')
				elif self.screen[i][j] == -2:
					print(self.ground,end='')
				elif self.screen[i][j] == ord(" "):
					print(" ",end='')
				elif self.screen[i][j] == ord("-"):
					print("-",end='')
				elif self.screen[i][j] == ord("_"):
					print("_",end='')
				elif self.screen[i][j] == ord("."):
					print(".",end='')
				elif self.screen[i][j] == ord("["):
					print("[",end='')
				elif self.screen[i][j] == ord(":"):
					print(":",end='')
				elif self.screen[i][j] == ord("]"):
					print("]",end='')
				elif self.screen[i][j] == ord("+"):
					print("+",end='')
				elif self.screen[i][j] == ord("|"):
					print("|",end='')
				elif self.screen[i][j] == ord("@"):
					print(self.herobullet,end='')
				elif self.screen[i][j] == ord("e"):
					print(self.enemybullet,end='')
				elif self.screen[i][j] == ord("S"):
					print("\033[34mS\033[0m",end='')
				elif self.screen[i][j] == 6:
					print(self.danger,end='')
				elif self.screen[i][j] == 99:
					print(self.coin,end='')			
			print('\\')
			
	def printonly(self,start,shield):
		for i in range(self.__rows):
			for j in range(start,min(start+100,self.__cols)):
				if self.screen[i][j] == 0:
					print(' ',end='')
				elif self.screen[i][j] == -1:
					print(self.sky,end='')
					# print(j%10,end='')
				elif self.screen[i][j] == -2:
					print(self.ground,end='')
				elif self.screen[i][j] == ord(" "):
					print(" ",end='')
				elif shield == -1 and self.screen[i][j] == ord("-"):
					print("\033[40m-\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == ord("_"):
					print("\033[40m_\033[0m",end='')
				elif shield == -1 and self.screen[i][j] == ord("."):
					print("\033[40m.\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == ord("-"):
					print("\033[44m-\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == ord("_"):
					print("\033[44m_\033[0m",end='')
				elif shield == 1 and self.screen[i][j] == ord("."):
					print("\033[44m.\033[0m",end='')
				elif self.screen[i][j] == ord("["):
					print("[",end='')
				elif self.screen[i][j] == ord(":"):
					print(":",end='')
				elif self.screen[i][j] == ord("]"):
					print("]",end='')
				elif self.screen[i][j] == ord("+"):
					print("+",end='')
				elif self.screen[i][j] == ord("|"):
					print("|",end='')
				elif self.screen[i][j] == ord("@"):
					print(self.herobullet,end='')
				elif self.screen[i][j] == ord("e"):
					print(self.enemybullet,end='')
				elif self.screen[i][j] == ord("m"):
					print(self.mmag,end='')
				elif self.screen[i][j] == ord("a"):
					print(self.amag,end='')
				elif self.screen[i][j] == ord("g"):
					print(self.gmag,end='')
				elif self.screen[i][j] == ord("S"):
					print("\033[34mS\033[0m",end='')
				elif self.screen[i][j] == 6:
					print(self.danger,end='')
				elif self.screen[i][j] == 99:
					print(self.coin,end='')	
			print('\\')
	
	def getscreen(self):
		return self.screen

	def setscreen(self, upd):
		self.screen = upd