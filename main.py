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

movemap = {'w': 0, 'd': 1, 'a': 2, 'q': -1, 'p': 5, '':-10}
# up,right,left,quit,shoot

l = 46
b = 1000

board = bg(l,b)
hero = mando(board.screen,l-4,3)
obstacles(board.screen,l,b)
check = checker()

col = 0
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
grav = 0
intensity = 0
speedup = 0

timeofstart = time.time()
print("Seconds since epoch =", timeofstart)	

while cou<60 and hero.lives > 0:
	print("\033[%d;%dH" % (0, 0))
	seconds = time.time()
	print("Seconds since epoch =", seconds)	

	print("Entered with score: ", hero.score, " and lives: ", hero.lives, " and time elapsed: ", round(seconds - timeofstart,2))
	# os.system("clear")
	hero.score += 1
	board.printonly(col)
	for i in range(speedup + 2):
		col += 1
		cou += 1
	move = user_input()
	if movemap[move] == -1:	
		print("Quitting")
		quit()
	print(move, "skvnw")
	if move not in movemap.keys():	move = ''#handles all other keys
	print(move, "skvnw")
	hero.x, hero.y = check.domove(board.screen, movemap[move], col, hero.x, hero.y, l, min(col+100,b))
	if move != 'w':	
		for i in range(intensity + 2):
			hero.x, hero.y, grav = check.down(board.screen, col, hero.x, hero.y, l, min(col+100,b), grav)
		if grav == 1 and hero.x == l-4:	
			grav = 0
			intensity = 0
		elif grav == 1: 
			pass# intensity += 1
	elif move == 'w' and grav == 1:
		grav = 1
		intensity = 0				
	#move down with var=1, var *=2 across iterations for i in var: move down till ground or i
	if check.limit(col, hero.x) == 1:	pass#move right
	if check.collision(col, board.screen, hero.x, hero.y, move, l, min(col+100,b))	== 1:	pass#dochange()
	else:	pass
	while hero.y <= col:		hero.x, hero.y = check.domove(board.screen, movemap['d'], col, hero.x, hero.y, l, min(col+100,b))


print("Done")