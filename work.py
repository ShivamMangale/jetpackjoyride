class checker:
	def __init__(self):
		pass

	def collision(self, start, screen, x, y, move, l, b):
		'''0===up
		   1===right
		   2===left'''
		if move == 0:
			if x == l + 2:	return 2
			elif screen[x-1][y:y+2] in [11,12,13]:	return -1
			elif screen[x-1][y:y+2] in [0,99]:	return 0
			else:		return 1
		elif move == 1:
			if y > (start + b) - 2:	return 10
			elif screen[x:x+2][y+3] in [11,12,13]:	return -1
			elif screen[x:x+2][y+3] in [0,99]:	return 0
			else:		return 1
		elif move == 2:
			if y == start: return 2
			elif screen[x:x+2][y-1] in [11,12,13]:	return -1 
			elif screen[x:x+2][y-1] in [11,12,13]:	return 0
			else:		return 1
		else:	return 1			