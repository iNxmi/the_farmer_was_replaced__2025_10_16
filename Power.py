import Utils, Move, Path, List, Planter, Drones, Harvest


planter = Planter.new()
def power():
	drones = set()
	for y in range(get_world_size()):
		Move.to((0, y))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			for position in Path.horizontal(y):
				Move.to(position)
				planter["set"](Entities.Sunflower)	
		
		drone = spawn_drone(execute)
		drones.add(drone)
		
	Move.to((0, 0))

	Drones.join(drones)
	drones = set()
		
	for level in range(15, 7 - 1, -1):
		
		def condition_function():
			return measure() == level
		
		Harvest.multi_threaded(condition_function)

Utils.initialize()
while True:
	power()