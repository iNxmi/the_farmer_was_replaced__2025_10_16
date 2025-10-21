import Move, Path, Planter, Thread, Bulk

planter_default = Planter.new()
def function_plant(entity, planter = planter_default):
	
	def execute(position_start):
		y = position_start[1]
		for position in Path.horizontal(y):
			Move.to(position)
			planter["set"](entity)
	
	return execute
	

def full(entity, planter = planter_default):
	blocked = set()
	path = Path.snake()
	positions = list(path)
	harvestable = set(path)
	
	execute = function_plant(entity, planter)
	Bulk.horizontal(execute)
	
	for position in positions:
		if position in blocked:
			continue

		Move.to(position)
		
		entity_companion, position_companion = get_companion()
		if position_companion in blocked:
			continue
			
		def execute():
			Move.to(position_companion)
			planter["set"](entity_companion)
			
			Move.to(position)
			
			while not can_harvest():
				pass
				
			harvest()
			
		harvestable.remove(position_companion)
		
		while num_drones() >= max_drones():
			pass
			
		thread = Thread.new(execute)
		thread["start"]()
		
		blocked.add(position)
		blocked.add(position_companion)