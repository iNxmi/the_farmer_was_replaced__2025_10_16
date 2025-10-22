import Bulk, Planter, Path, Utils, Move

planter = Planter.new()
planter["set_forcing"](True)
planter["set_watering_threshold"](0.5)

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
			
Utils.initialize(31)
Bulk.horizontal(function)