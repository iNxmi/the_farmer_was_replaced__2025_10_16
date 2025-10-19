import Utils, Move, Path, Planter, List, Drones


def pumpkin():
	planter = Planter.new()
	drones = set()
	for y in range(get_world_size()):
		Move.to((0, y))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			positions = Path.horizontal(y)
			while len(positions) > 0:
				for position in list(positions):
					Move.to(position)
					
					if (get_entity_type() == Entities.Pumpkin) and can_harvest():
						positions.remove(position)
						continue
						
					planter["set"](Entities.Pumpkin)
		
		drone = spawn_drone(execute)
		drones.add(drone)
		
	Move.to((0,0))

	Drones.join(drones)
				
	harvest()


Utils.initialize()
while True:
	pumpkin()
