import List, Math

def snake(size = get_world_size()):
	positions = []
	
	range_default = range(size)
	range_reversed = range(size - 1, -1, -1)

	for y in range_default:
		xRange = range_default
		if y % 2 != 0:
			xRange = range_reversed
		
		for x in xRange:
			position = (x, y)
			positions.append(position)
			
	return positions


def default(size = get_world_size()):
	positions = []
	
	rng = range(size)
	for y in rng:
		for x in rng:
			position = (x, y)
			positions.append(position)
			
	return positions
	
def horizontal(y):
	positions = []
	for x in range(get_world_size()):
		positions.append((x, y))
	
	return positions
	
def vertical(x):
	positions = []
	for y in range(get_world_size()):
		positions.append((x, y))
	
	return positions

def to(destination):
	pass

# obstacles = set() of positions where drone cannot move
def a_star(start, goal, obstacles):
	
	def h(start, goal):
		return abs(start[0] - goal[0]) + abs(start[1] - goal[1])
	
	g_score = {start: 0}
	f_score = {start: h(start, goal) }
	
	open = set()
	open.add(start)
	
	came_from = dict()
	
	while len(open) > 0:
		h_open = dict()
		values = set()
		for node in open:
			value = h(start, node)
			h_open[value] = node
			values.add(value)
			
		current_key = Math.min(values)
		current = h_open[current_key]
		
		if current == goal:
			result = []
			while current in came_from:
				result.append(current)
				current = came_from[current]
			result.append(start)
			reversed = List.get_reversed(result)
			return reversed
			
		open.remove(current)
		
		for delta in {(0, 1), (1, 0), (0, -1), (-1, 0)}:
			position_neighbor = ((current[0] + delta[0]), (current[1] + delta[1]))
			
			if position_neighbor in obstacles:
				continue
			if position_neighbor[0] < 0:
				continue
			if position_neighbor[1] < 0:
				continue
			if position_neighbor[0] >= get_world_size():
				continue
			if position_neighbor[1] >= get_world_size():
				continue
			
			tentative_g = g_score[current] + 1
			if position_neighbor not in g_score or tentative_g < g_score[position_neighbor]:
				came_from[position_neighbor] = current
				g_score[position_neighbor] = tentative_g
				f_score[position_neighbor] = tentative_g + h(position_neighbor, goal)
				
				if position_neighbor not in open:
					open.add(position_neighbor)
			
	return None