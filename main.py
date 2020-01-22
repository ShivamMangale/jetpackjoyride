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
from finalscreen import finalscreen

movemap = {'w': 0, 'd': 1, 'a': 2, 'q': -1, 'p': 5, '':-10, ' ':100}

l = 40
b = 1000

timeofstart = time.time()
board = bg(l,b)
hero = mando(board,l-4,3)
obst = obstacles(board, l, b)
maglocx, maglocy = obst.magnet(board, l, b)
speedx, speedy = obst.speed(board, l, b)
en = enemy(board, l-4, b-4, timeofstart)

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

while col<1000 and hero.getlives() > 0 and en.getlives() > 0:
	seconds = time.time()

	print("Score: ", hero.getscore()) 
	print("Hero's lives: ", str(hero.getlives())," and Enemy's lives: ", en.getlives())
	print("Time elapsed: ", round(seconds - timeofstart,2))
	print("\033[%d;%dH" % (0, 0))
	board.printonly(col,hero.getflagshield())

	while hero.gety() <= col + hero.getspeedup():	hero.domove(board.getscreen(), movemap['d'], col, l, min(col+100,b))


	if col < 900:
		col += hero.getspeedup()

	hero.updateshield()

	move = user_input()

	if move not in movemap.keys():	move = ''

	if movemap[move] == -1:	
		print("Quitting")
		quit()
	elif movemap[move] == 100:
		hero.tryshield()

	if movemap[move] == 5:
		hero.shoot()

	hero.updatebullets(en, board.getscreen(), col, l, b)

	for i in range(int((hero.getspeedup()+1)/2)):
		hero.domove(board.getscreen(), movemap[move], col, l, min(col+100,b))

	hero.gravity(board.getscreen(), col, l, min(col + 100,b), move)

	hero.isspeed(speedx, speedy)

	if col > 900:
		en.enemyreached()
			
	en.checkifenemyshoot()
		
	en.updatebullets(hero, board)

	en.move(board, hero.getx(), b)

	hero.checkmagnet(board.getscreen(), col, l, min(col+100,b), movemap, maglocx, maglocy)

if en.getlives() == 0:
	fin = finalscreen()
	print("\033[%d;%dH" % (0, 0))
	fin.printit()
else:
	print("\033[%d;%dH" % (0, 0))
	print("GAME OVER")
		
print("Done")