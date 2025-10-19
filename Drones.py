import List, Constants, Random

def join(lst):
	drones = list(lst)
	while len(drones) > 0:
		for drone in drones:
			if has_finished(drone):
				drones.remove(drone)

def spawn(function):
	
	def execute():
		hat = Random.list(Constants.HATS)
		change_hat(hat)
		
		function()
	
	return spawn_drone(execute)
	
	