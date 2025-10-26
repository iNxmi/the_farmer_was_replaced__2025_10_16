import Utils, Move, Path, Planter, List, Bulk

def simple():
	planter = Planter.new()
	positions = Path.snake()
	while len(positions) > 0:
		for position in list(positions):
			Move.to(position)
			
			if (get_entity_type() == Entities.Pumpkin) and can_harvest():
				positions.remove(position)
				continue
			
			planter["set"](Entities.Pumpkin)

def parallel():
	pass

if __name__ == "__main__":
	Utils.initialize()
	
	planter = Planter.new()
	planter["set_minimum_water"](0.8)
	def function_plant(position_start):
		y = position_start[1]
		positions = Path.horizontal(y)
		while len(positions) > 0:
			for position in list(positions):
				Move.to(position)
				
				if (get_entity_type() == Entities.Pumpkin) and can_harvest():
					positions.remove(position)
					continue
				
				planter["set"](Entities.Pumpkin)
	
	Bulk.horizontal(function_plant)
	harvest()

	Utils.initialize()
	while True:
		Bulk.horizontal(function_plant)
		harvest()
