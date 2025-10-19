import Utils, Move, Path, Plant, List, Drones


def cactus():
	drones = set()
	for y in range(get_world_size()):
		Move.to((0, y))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			for position in Path.horizontal(y):
				Move.to(position)
				Plant.set(Entities.Cactus)
				
			for iteration in range(get_world_size() - 1, -1, -1):
				swapped = False
				for x in range(iteration):
					Move.to((x, y))
		
					value = measure()
					value_right = measure(East)
					
					if value > value_right:
						swap(East)
						swapped = True
						
				if not swapped:
					break
				
		drone = spawn_drone(execute)
		drones.add(drone)

	Move.to((0, 0))

	Drones.join(drones)
	drones = set()

	for x in range(get_world_size()):
		Move.to((x, 0))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			for iteration in range(get_world_size() - 1, -1, -1):
				swapped = False
				for y in range(iteration):
					Move.to((x, y))
		
					value = measure()
					value_right = measure(North)
					
					if value > value_right:
						swap(North)
						swapped = True
						
				if not swapped:
					break
				
		drone = spawn_drone(execute)
		drones.add(drone)
		
	Move.to((0,0))

	Drones.join(drones)
				
	harvest()

Utils.initialize()
while True:
	cactus()
	
