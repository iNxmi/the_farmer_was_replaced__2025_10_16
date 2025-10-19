import Utils, Move, Path, Planter, List, Drones

planter = Planter.new()
def cactus():
	drones = set()
	for y in range(get_world_size()):
		Move.to((0, y))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			global y
			for position in Path.horizontal(y):
				Move.to(position)
				planter["set"](Entities.Cactus)
			
			Move.to((0, y))

			for iteration in range(get_world_size()):
				swapped = False
				for x in range(get_pos_x(), get_world_size() - iteration - 1, 1):
					position = (x, y)
					Move.to(position)
					
					if measure() > measure(East):
						swap(East)
						swapped = True
				
				if not swapped:
					break

				for x in range(get_pos_x(), 0 + iteration, -1):
					position = (x, y)
					Move.to(position)
					
					if measure() < measure(West):
						swap(West)
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
			for iteration in range(get_world_size()):
				swapped = False
				for y in range(get_pos_y(), get_world_size() - iteration - 1, 1):
					position = (x, y)
					Move.to(position)
					
					if measure() > measure(North):
						swap(North)
						swapped = True
				
				if not swapped:
					break

				for y in range(get_pos_y(), 0 + iteration, -1):
					position = (x, y)
					Move.to(position)
					
					if measure() < measure(South):
						swap(South)
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
	
