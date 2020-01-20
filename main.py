from colorama import Fore, Back, Style
from bg import bg
import os
from mando import mando
from obstacles import obstacles
from getch import _getChUnix as getChar
import signal
from alarmexception import AlarmException
import sys 
import time
from enemy import enemy

movemap = {'w': 0, 'd': 1, 'a': 2, 'q': -1, 'p': 5, '':-10, ' ':100}
# up,right,left,quit,shoot,everything else,shield

l = 40
b = 1000

timeofstart = time.time()
board = bg(l,b)
hero = mando(board.screen,l-4,3)
obst = obstacles(board.screen, l, b)
maglocx, maglocy = obst.magnet(board.screen, l, b)
speedx, speedy = obst.speed(board.screen, l, b)
en = enemy(board.screen, l-4, b-4, timeofstart)

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

col = 0
grav = 0
hero.speedup = 1
print("Seconds since epoch =", timeofstart)	
flagshield = -1
timeofshield = 0
shieldable = 1
timeofshieldend = -1
speedinit = 0
bullets = []

while col<1000 and hero.lives > 0 and en.lives > 0:
	seconds = time.time()

	print("Entered with score: ", hero.score, " and hero's lives: ", hero.lives, " and time elapsed: ", round(seconds - timeofstart,2), " and col: ", col, " while enemy's lives: ", en.lives)
	print("\033[%d;%dH" % (0, 0))

	while hero.y <= col:	hero.domove(board.screen, movemap['d'], col, l, min(col+100,b))

	board.printonly(col,flagshield)

	if col < 900:
		col += hero.speedup

	flagshield = hero.updateshield()

	move = user_input()

	if move not in movemap.keys():	move = ''#handles all other keys

	if movemap[move] == -1:	
		print("Quitting")
		quit()
	elif movemap[move] == 100:
		flagshield = hero.tryshield()

	if movemap[move] == 5:
		hero.shoot()

	en.lives -= hero.updatebullets(board.screen, col, l, b)

	for i in range(int((hero.speedup+1)/2)):
		hero.domove(board.screen, movemap[move], col, l, min(col+100,b))

	hero.gravity(board.screen, col, l, min(col + 100,b), move)

	hero.isspeed(speedx, speedy)

	if col > 900:
		en.enemyreached()
			
	en.checkifenemyshoot()
		
	hero.lives -= en.updatebullets(board.screen, hero.x, hero.y, flagshield)

	en.move(board.screen, hero.x, b)
		
	if maglocy >= col and maglocy < col + 100:
		mag = [ord('m'), ord('a'), ord('g')]
		for i in range(3):
			board.screen[maglocx][maglocy - col + 1] = ord(" ")
			board.screen[maglocx][maglocy - col] = mag[i]
		if hero.y <= maglocy:
			hero.domove(board.screen, movemap['d'], col, l, min(col+100,b))
		else:
			hero.domove(board.screen, movemap['a'], col, l, min(col+100,b))


print("Done")