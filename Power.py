import Bulk, Planter, Path, Utils, Move

planter = Planter.new()
planter["set_forcing"](True)
planter["set_watering_threshold"](0.75)

def function(position_start):
	y = position_start[1]
	path = Path.horizontal(y)
	while True:
		for position in path:
			Move.to(position)
			
			if measure() == 15:
				if not can_harvest():
					continue 
					
				harvest()
				
			planter["set"](Entities.Sunflower)
			
def function_new(position_start):
	y = position_start[1]
	path = Path.horizontal(y)
	length = len(path)
	while True:
		for index in range(length):
			position = path[index]
			Move.to(position)
			
			if measure() == 15:
				if not can_harvest():
					continue 
					
				harvest()
				
			planter["set"](Entities.Sunflower)

		for index in range(length - 1, -1, -1):
			position = path[index]
			Move.to(position)
			
			if measure() == 15:
				if not can_harvest():
					continue 
					
				harvest()
				
			planter["set"](Entities.Sunflower)
			
Bulk.horizontal(function_new)