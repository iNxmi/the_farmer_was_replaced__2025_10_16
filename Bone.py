import Utils, Path, Move

set_world_size(10)
while True:
	Utils.initialize()
	change_hat(Hats.Dinosaur_Hat)
	
	tail = []
	while True:
		goal = measure()
		position = (get_pos_x(), get_pos_y())
		path = Path.a_star(position, goal, set(tail))
		for position in path:
			Move.to(position)

			if len(tail) > 0:
				tail.pop(0)
				tail.append(position)
				
			quick_print(tail)
				
		tail.append((get_pos_x(), get_pos_y()))

		