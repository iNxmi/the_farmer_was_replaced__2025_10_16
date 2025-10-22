import Bulk, Move, Path, Utils

def function(position_start):
	y = position_start[1]
	path = Path.horizontal(y)
	length = len(path)
	while True:
		for index in range(length):
			position = path[index]
			Move.to(position)
			harvest()

		for index in range(length - 1, -1, -1):
			position = path[index]
			Move.to(position)
			harvest()

Utils.initialize(31)
Bulk.horizontal(function)