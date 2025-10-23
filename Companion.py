import Move, Path, Planter, Thread, Bulk


def parallel(entity):
	
	def generate_path():
		positions = []
		for y in range(6):
			for x in range(6):
				if x == 0 and y == 0:
					continue
				if x == 5 and y == 0:
					continue
				if x == 0 and y == 5:
					continue
				if x == 5 and y == 5:
					continue
				
				position = (3 + x * 5, 3 + y * 5)
				positions.append(position)
				
		return positions
	
	planter = Planter.new()
	planter["set_forcing"](True)
	planter["set_minimum_water"](0.75)
	planter_companion = Planter.new()
	def execute(position_start):
		while True:
			planter["set"](entity)
			
			entity_companion, position_companion = get_companion()
			if abs(position_companion[0] - position_start[0]) >= 3:
				continue
			if abs(position_companion[1] - position_start[1]) >= 3:
				continue
	
			Move.to(position_companion)
			planter_companion["set"](entity_companion)
			
			Move.to(position_start)
			if not can_harvest():
				use_item(Items.Fertilizer)
				use_item(Items.Weird_Substance)
				
			harvest()
	
	path = generate_path()
	Bulk.path(path, execute)