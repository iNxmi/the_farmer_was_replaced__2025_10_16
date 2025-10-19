import Move, Path, Planter, Drones, Harvest

planter_default = Planter.new()
def full(entity, planter = planter_default):
	blocked = set()
	path = Path.snake()
	positions = list(path)
	harvest = set(path)
	for position in positions:
		if position in blocked:
			continue

		Move.to(position)
		planter["set"](entity)
		
		entity_companion, position_companion = get_companion()
		if position_companion in blocked:
			continue
			
		def execute():
			Move.to(position_companion)
			planter["set"](entity_companion)
			
			Move.to(position)
			Harvest.blocking()
			
		harvest.remove(position_companion)
		
		spawn_drone(execute)
		
		blocked.add(position)
		blocked.add(position_companion)