class Rover:

	def __init__(self,x,y,elevation):
		"""
		Initialises the rover
		"""
		self.elv=elevation
		self.x=x
		self.y=y
		self.battery=100


	def move(self,direction, cycles):
		"""
		Moves the rover on the planet
		"""
		pass

	def wait(self, cycles):
		"""
		The rover will wait for the specified cycles
		"""
		self.battery += int(cycles)
		if self.battery >= 100:
			self.battery = 100
