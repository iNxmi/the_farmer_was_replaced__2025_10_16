import Move, Drones, Plant, Harvest, Utils, Path


Utils.initialize()
size = get_world_size() // 2

threads = set()
for y in range(get_world_size()):
	Move.to((0, y))
	
	while num_drones() >= max_drones():
		pass
	
	def execute():
		for position in Path.horizontal(y):
				Move.to(position)
			
				till()
	
	thread = spawn_drone(execute)
	threads.add(thread)
	
Drones.join(threads)
threads = set()

while True:
	Move.to((size, size))

	if get_entity_type() == Entities.Carrot:
		while not can_harvest():
			pass
			
	harvest()
	Plant.set(Entities.Carrot)
	companion_entity, companion_position = get_companion()
	Move.to(companion_position)
	Plant.set(companion_entity)