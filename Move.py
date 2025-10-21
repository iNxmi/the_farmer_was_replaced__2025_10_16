def origin():
	to((0, 0))

def to(position):
	x = position[0]
	to_x(x)
	
	y = position[1]
	to_y(y)
	
def to_x(destination):
	drone = get_pos_x()
	if drone == destination:
		return

	delta = destination - drone
	
	distance = abs(delta)
	direction = East
	if delta < 0:
		direction = West
		
	for i in range(distance):
		move(direction)
		

def to_y(destination):
	drone = get_pos_y()
	if drone == destination:
		return
	
	delta = destination - drone
	
	distance = abs(delta)
	direction = North
	if delta < 0:
		direction = South
		
	for i in range(distance):
		move(direction)