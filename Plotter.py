import Move, Math, Path, Utils, Bulk

def plot(function, origin = (0, 0), scale = 1):
	grid = {}
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			grid[(x, y)] = y - (function(x - origin[0]) + origin[1])
	
	def render_row(position_start):
		y = position_start[1]
		for position in Path.horizontal(y):
			Move.to(position)
			
			sign = Math.sign(grid[position])
			if sign == 0:
				if get_ground_type() != Grounds.Soil:
					till()
				continue
			
			signs = set()
			for delta in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
				neighbor = (position[0] + delta[0], position[1] + delta[1])
				
				if neighbor[0] < 0 or neighbor[0] >= get_world_size():
					continue
				if neighbor[1] < 0 or neighbor[1] >= get_world_size():
					continue		
		
				sign_neighbor = Math.sign(grid[neighbor])
				signs.add(sign_neighbor)
				
				if (1 in signs) and (-1 in signs):
					if get_ground_type() != Grounds.Soil:
						till()
					break
	
	Bulk.horizontal(render_row)

def function(x):
	return 3
	
Utils.initialize()
plot(function, (16, 16))
	