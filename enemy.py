from person import person

class enemy(person):
	def __init__(self,x,y):
		super().__init__(x,y)
		self.looks = [[ord("^")]]#add more
		#put on map, refer obstacles