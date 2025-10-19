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

def a_star(destination):
	pass