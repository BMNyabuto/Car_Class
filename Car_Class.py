class Car(object):
	No_of_doors = 0
	wheels = 0
	speed = 0
	def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
		self.name = name
		self.model = model
		self.car_type = car_type
    
	def num_of_doors(self):
		if self.name is 'Koenigsegg' :
			self.No_of_doors = 2
			return self.No_of_doors

		elif self.name is 'Porsche':
			self.No_of_doors = 2
			return self.No_of_doors

		else:
			self.No_of_doors = 4
			return self.No_of_doors
	def num_of_wheels(self):	
		
		if self.car_type == 'trailer':	
			wheels = 8
			return wheels
			
		else:	
			wheels = 4
			return  wheels

	def drive(self, x):
		
		if self.car_type == 'trailer':
			self.speed = 77
			return self.speed
		else:
			self.speed = int(math.pow(x,3))
			return self.speed
		