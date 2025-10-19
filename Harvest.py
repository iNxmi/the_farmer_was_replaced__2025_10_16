import Drones, Move, Path

def blocking():
	while not can_harvest():
		pass
		
	harvest()

def condition_function_default():
	return True

def multi_threaded(condition_function = condition_function_default):
	threads = set()
	for y in range(get_world_size()):
		Move.to((0, y))
		
		while num_drones() >= max_drones():
			pass
		
		def execute():
			for position in Path.horizontal(y):
				Move.to(position)
				
				if not condition_function():
					continue
					
				blocking()
		
		thread = spawn_drone(execute)
		threads.add(thread)
		
	Move.to((0, 0))

	Drones.join(threads)
	threads = set()
	