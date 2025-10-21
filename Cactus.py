import Utils, Move, Path, Planter, List, Bulk

planter = Planter.new()
def function_plant(position_start):
	y = position_start[1]
	for position in Path.horizontal(y):
		Move.to(position)
		planter["set"](Entities.Cactus)

def function_horizontal(position_start):
		y = position_start[1]
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
	
def function_vertical(position_start):
	x = position_start[0]

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

def cactus():
	Bulk.horizontal(function_plant)
	Bulk.horizontal(function_horizontal)
	Bulk.vertical(function_vertical)
	
	harvest()

Utils.initialize()
while True:
	cactus()
	
