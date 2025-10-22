import Utils, Path, Move, Constants, Random, Logger, List

log = Logger.new("Bone")

def bone_defined_path():
	path = [(0, 0)]
	
	range_default = range(1, get_world_size(), 1)
	range_reversed = range(get_world_size() - 1, 0, -1)

	for y in range(get_world_size()):
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
		Move.origin()
		change_hat(Hats.Dinosaur_Hat)
		count = 1
		time_start_all = get_time()
		while can_move(North) or can_move(East) or can_move(South) or can_move(West):
			time_start = get_time()
			
			start = List.get_index(path, (get_pos_x(), get_pos_y()))
			for index in range(start, len(path), 1):
				position = path[index]
				Move.to(position)
				
				apple = measure()
				if apple == None:
					continue
					
				y_goal = apple[1]
				if y_goal % 2 != 0:
					y_goal -= 1
				if apple[1] < position[1]:
					while get_pos_x() > 0:
						if can_move(West):
							move(West)
						elif can_move(East):
							move(East)
						else:
							move(North)
					while get_pos_y() > y_goal:
						move(South) 
						
					move(East)
					
					break
			
			time_current = get_time()
			message = "Total=" + str(time_current - time_start_all) + " Average=" + str((time_current - time_start_all) / count) + " Last=" + str(time_current - time_start) 
			log["info"](message)
			count += 1
				
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

		