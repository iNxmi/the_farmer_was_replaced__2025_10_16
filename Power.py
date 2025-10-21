import Utils, Move, Path, Planter, Bulk

planter = Planter.new()
planter["set_watering_threshold"](0.25)

def function_plant(position_start):
	y = position_start[1]
	for position in Path.horizontal(y):
		Move.to(position)
		planter["set"](Entities.Sunflower)

def function_harvest(level):
	
	def execute(position_start):
		y = position_start[1]
		for position in Path.horizontal(y):
			Move.to(position)
			
			if measure() != level:
				continue
				
			while not can_harvest():
				pass
				
			harvest()
	
	return execute
	

def power():
	Bulk.horizontal(function_plant)
	
	for level in {15, 14, 13, 12, 11, 10, 9, 8, 7}:
		Bulk.horizontal(function_harvest(level))

Utils.initialize()
while True:
	power()