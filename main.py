from colorama import Fore, Back, Style
from bg import bg
import os
from mando import mando
from work import checker
from obstacles import obstacles
from getch import _getChUnix as getChar
import signal
from alarmexception import AlarmException
import sys 
import time
from enemy import enemy

movemap = {'w': 0, 'd': 1, 'a': 2, 'q': -1, 'p': 5, '':-10, ' ':100}
# up,right,left,quit,shoot

l = 40
b = 1000

board = bg(l,b)
hero = mando(board.screen,l-4,3)
obst = obstacles(board.screen, l, b)
maglocx, maglocy = obst.magnet(board.screen, l, b)
speedx, speedy = obst.speed(board.screen, l, b)
check = checker()

os.system("clear")
def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

def user_input(timeout=0.1):
    ''' input method '''
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getChar()()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
cou = 0
col = 0
grav = 0
speedup = 1

timeofstart = time.time()
print("Seconds since epoch =", timeofstart)	
flagshield = -1
timeofshield = 0
shieldable = 1
timeofshieldend = -1
speedinit = 0
en = enemy(board.screen, l-4, b-4)
bulletcount = 0
details = []
timeforenemybullet = timeofstart + 10000
reachedenemy = -1
enemybullet = []

while cou<1000 and hero.lives > 0 and en.lives > 0:
	seconds = time.time()
	print("Entered with score: ", hero.score, " and hero's lives: ", hero.lives, " and time elapsed: ", round(seconds - timeofstart,2), " and col: ", col, " while enemy's lives: ", en.lives)
	print("\033[%d;%dH" % (0, 0))
	board.printonly(col,flagshield)
	if cou < 903:
		for i in range(speedup):
			col += 1
			cou += 1
	move = user_input()
	if seconds - timeofshieldend > 10:
		shieldable = 1
	if move not in movemap.keys():	move = ''#handles all other keys
	if movemap[move] == -1:	
		print("Quitting")
		quit()
	elif movemap[move] == 100 and flagshield == -1 and shieldable == 1:
		flagshield = 1
		timeofshield = time.time()
	elif movemap[move] == 100 and flagshield == 1:	pass
	if flagshield == 1 and seconds - timeofshield > 10:	
		flagshield = -1
		timeofshieldend = time.time()
		shieldable = 0
	if movemap[move] == 5:
		details.append([hero.x+1,hero.y+3])
		bulletcount += 1
	for i in range(speedup):	
		for shots in details:
			if shots[1] < b-3:
				if board.screen[shots[0]][shots[1] + 1] == 6 or board.screen[shots[0]][shots[1] + 2] == 6 or board.screen[shots[0]][shots[1] + 3] == 6:
					for i in range(max(2,shots[0]-7),min(l-2,shots[0]+7)):
						for j in range(max(col,shots[1]-7),min(min(col+100,shots[1]+7),b)):
							if board.screen[i][j] == 6:
								board.screen[i][j] = ord(" ")
					board.screen[shots[0]][shots[1]] = ord(" ")
					shots[0],shots[1] = b + 100, b + 100
				elif board.screen[shots[0]][shots[1] + 1] == 99 or board.screen[shots[0]][shots[1] + 2] == 99 or board.screen[shots[0]][shots[1] + 3] == 99:
					board.screen[shots[0]][shots[1]] = ord(" ")
					hero.score += 1
					for i in range(shots[1] + 1,shots[1] + 4):
						if board.screen[shots[0]][i] == 99:
							for j in range(i,i+3):
								board.screen[shots[0]][j] = ord(" ")
					shots[0],shots[1] = b + 100, b + 100
				elif board.screen[shots[0]][shots[1] + 1] == ord("+") or board.screen[shots[0]][shots[1] + 2] == ord("+") or board.screen[shots[0]][shots[1] + 3] == ord("+") or board.screen[shots[0]][shots[1] + 1] == ord("[") or board.screen[shots[0]][shots[1] + 2] == ord("[") or board.screen[shots[0]][shots[1] + 3] == ord("["):
					en.lives -= 1
					board.screen[shots[0]][shots[1]] = ord(" ")
					shots[0], shots[1] = b + 100,b + 100
				else:
					board.screen[shots[0]][shots[1]] = ord(" ")
					board.screen[shots[0]][shots[1] + 1] = ord(" ")
					board.screen[shots[0]][shots[1] + 2] = ord(" ")
					board.screen[shots[0]][shots[1] + 3] = ord("@")
					shots[1] = shots[1] + 3
					if shots[1] > col + 100:	
						board.screen[shots[0]][shots[1]] = ord(" ")
						shots[0], shots[1] = b + 100,b + 100
			elif shots[1] != b + 100:
				board.screen[shots[0]][shots[1]] = ord(" ")
				shots[0], shots[1] = b + 100,b + 100

	for i in range(int((speedup+1)/2)):
		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap[move], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	if move != 'w':	
		hero.x, hero.y, grav, hero.score, hero.lives = check.down(board.screen, col, hero.x, hero.y, l, min(col+100,b), grav, hero.score, hero.lives, flagshield)
		if grav == 1 and hero.x == l-4:	
			grav = 0
	elif move == 'w' and grav == 1:
		grav = 0
	#move down with var=1, var *=2 across iterations for i in var: move down till ground or i
	while hero.y <= col:		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	if speedx == hero.x or speedx == hero.x + 1 or speedx == hero.x + 2:
		if speedy == hero.y or speedy == hero.y + 1 or speedy == hero.y + 2:
			speedup = 5
			speedinit = time.time()

	if speedup == 5 and seconds - speedinit > 17:
		speedup = 1
	if cou > 900 and reachedenemy == -1:
		timeforenemybullet = time.time()
		reachedenemy = 1
	if seconds - timeforenemybullet > 1:
		for i in range(3):
			enemybullet.append([en.x + i, en.y - 1])
		timeforenemybullet = time.time()
	for i in enemybullet:
		if i[1] > 900:
			if hero.x <= i[0] and hero.x + 3 > i[0]:
				if hero.y <= i[1] and hero.y + 3 > i[1]:
					if flagshield == -1:
						hero.lives -= 1
					board.screen[i[0]][i[1]] = ord(" ")
					i[0], i[1] = 0, 0
			board.screen[i[0]][i[1]] = ord(" ")
			i[1] -= 3
			board.screen[i[0]][i[1]] = ord("e")
		else:
			i[0], i[1] = 20, 100
	if cou > 900: 
		en.x = en.move(board.screen, col, en.x, hero.x, l, b)
	if maglocy >= col and maglocy < col + 100:
		mag = [ord('m'), ord('a'), ord('g')]
		for i in range(3):
			board.screen[maglocx][maglocy - col + 1] = ord(" ")
			board.screen[maglocx][maglocy - col] = mag[i]
		if hero.y <= maglocy:
			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
		else:
			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['a'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)


print("Done")