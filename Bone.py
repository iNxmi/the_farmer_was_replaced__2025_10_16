import Utils, Path, Move, Constants, Random


def bone_defined_path():
	path = []
	
	range_default = range(1, get_world_size(), 1)
	range_reversed = range(get_world_size() - 1, 0, -1)

	for y in range_default:
		xRange = range_default
		if y % 2 != 0:
			xRange = range_reversed
		
		for x in xRange:
			position = (x, y)
			path.append(position)
			
	for y in range(get_world_size() - 1, -1, -1):
		position = (0, y)
		path.append(position)

	while True:
		Move.to((0, 0))
		change_hat(Hats.Dinosaur_Hat)
		while can_move(North) or can_move(East) or can_move(South) or can_move(West):
			Move.to((0, 0))			
			for position in path:
				Move.to(position)
				
		change_hat(Random.list(Constants.HATS))

		
Utils.initialize()
while True:
	bone_defined_path()


def bone_a_star():
	set_world_size(10)
	while True:
		Utils.initialize()
		change_hat(Hats.Dinosaur_Hat)
		
		tail = []
		while True:
			goal = measure()
			if goal == None:
				break
	
			position = (get_pos_x(), get_pos_y())
			path = Path.a_star(position, goal, set(tail))
			if path == None:
				break
			
			for index in range(len(path)):
				Move.to(path[index])
	
				if index >= 1 and len(tail) > 0:
					tail.pop(0)
					tail.append(path[index - 1])
					
			tail.append((get_pos_x(), get_pos_y()))

		