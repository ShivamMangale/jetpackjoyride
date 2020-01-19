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

movemap = {'w': 0, 'd': 1, 'a': 2, 'q': -1, 'p': 5, '':-10, ' ':100}
# up,right,left,quit,shoot

l = 40
b = 1000

board = bg(l,b)
hero = mando(board.screen,l-4,3)
obst = obstacles(board.screen, l, b)
maglocx, maglocy = obst.magnet(board.screen, l, b)
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
speedup = -1

timeofstart = time.time()
print("Seconds since epoch =", timeofstart)	
flagshield = -1
timeofshield = 0
shieldable = 1
timeofshieldend = -1

while cou<600 and hero.lives > 0:
	seconds = time.time()
	print("Entered with score: ", hero.score, " and lives: ", hero.lives, " and time elapsed: ", round(seconds - timeofstart,2))
	print("\033[%d;%dH" % (0, 0))
	board.printonly(col,flagshield)
	for i in range(speedup + 2):
		col += 1
		cou += 1
	move = user_input()
	if seconds - timeofshieldend > 10:
		shieldable = 1
	if movemap[move] == -1:	
		print("Quitting")
		quit()
	elif movemap[move] == 100 and flagshield == -1 and shieldable == 1:
		# check.enableshield(board.screen, col, hero.x, hero.y, l, min(col+100,b))
		flagshield = 1
		timeofshield = time.time()
	elif movemap[move] == 100 and flagshield == 1:	pass
	if flagshield == 1 and seconds - timeofshield > 10:	
		# check.disableshield(board.screen, col, hero.x, hero.y, l , min(col+100,b))
		flagshield = -1
		timeofshieldend = time.time()
		shieldable = 0

	if move not in movemap.keys():	move = ''#handles all other keys
	hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap[move], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	if move != 'w':	
		hero.x, hero.y, grav, hero.score, hero.lives = check.down(board.screen, col, hero.x, hero.y, l, min(col+100,b), grav, hero.score, hero.lives, flagshield)
		if grav == 1 and hero.x == l-4:	
			grav = 0
	elif move == 'w' and grav == 1:
		grav = 0
	#move down with var=1, var *=2 across iterations for i in var: move down till ground or i
	while hero.y <= col:		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# if hero.y >= maglocy - 100 and hero.y <= maglocy + 100 :
	# 	if hero.y < maglocy:
	# 		if hero.x > maglocx: 
	# 			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['w'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# 			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# 		elif hero.x < maglocx:
	# 			hero.x, hero.y, hero.score, hero.lives = check.down(board.screen, col, hero.x, hero.y, l, min(col+100,b), 1, hero.score, hero.lives, flagshield)
	# 			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# 		else:
	# 			hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# 	elif hero.y == maglocy:
	# 		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)

	# 	else:
	# 		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['w'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)
	# 		hero.x, hero.y, hero.score, hero.lives = check.domove(board.screen, movemap['a'], col, hero.x, hero.y, l, min(col+100,b), hero.score, hero.lives, flagshield)


print("Done")