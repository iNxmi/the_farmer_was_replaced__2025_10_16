import Thread, Move, Path, Logger

log = Logger.new("Bulk")

def path(path, function):
	threads = list()

	Move.origin()
	for position in path:
		Move.to(position)
		
		def execute():
			function(position)
		
		while num_drones() >= max_drones():
			pass
			
		thread = Thread.new(execute)
		threads.append(thread)
		thread["start"]()

	Move.origin()

	while len(threads) > 0:
		thread = threads.pop()
		thread["join"]()

def horizontal(function):
	positions = Path.vertical(0)
	path(positions, function)
	
def vertical(function):
	positions = Path.horizontal(0)
	path(positions, function)
