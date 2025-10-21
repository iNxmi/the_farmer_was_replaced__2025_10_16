import Thread, Move, Path

def path(path, function):
	threads = list()
	
	Move.origin()
	for position in path:
		Move.to(position)
		
		while num_drones() >= max_drones():
			pass
			
		def execute():
			function(position)
		
		thread = Thread.new(execute)
		threads.append(thread)
		thread["start"]()
	Move.origin()

	for thread in threads:
		thread["join"]()
		threads.remove(thread)

path_vertical = Path.vertical(0)
def horizontal(function):
	path(path, path_vertical)
	
path_horizontal = Path.horizontal(0)
def vertical(function):
	path(path_horizontal, function)
