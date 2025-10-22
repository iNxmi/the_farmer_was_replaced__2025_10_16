import List, Constants, Random, Logger

log = Logger.new("Thread")

def new(function):
	
	random_hat = True
	def get_random_hat():
		global random_hat
		return random_hat
	def set_random_hat(value):
		global random_hat
		random_hat = value
		
	drone = None
	def get_drone():
		global drone
		return drone
	def set_drone(value):
		global drone
		drone = value
		
	def execute():
		if get_random_hat():
			hat = Random.list(Constants.HATS)
			change_hat(hat)
			
		function()
		
	def start():
		if get_drone() != None:
			log["error"]("Thread has already been started")
			return
			
		if num_drones() >= max_drones():
			log["error"]("Max number of drones has already been reached" + str(max_drones()))
			return
		
		drone = spawn_drone(execute)
		set_drone(drone)
	
	def join():
		drone = get_drone()
		if drone == None:
			log["error"]("Thread has not been started")
			return
		
		value = wait_for(drone)
		return value
	
	return {
		"get_random_hat": get_random_hat,
		"set_random_hat": set_random_hat,

		"get_drone": get_drone,
		
		"start": start,
		"join": join
	}
		
		