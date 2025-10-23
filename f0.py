import Bulk, Move, Path, Planter, Constants, Utils

planter = Planter.new()
def spawn(size):
	planter["set"](Entities.Bush)
	substance = size * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	use_item(Items.Weird_Substance, substance)

def scan(size):
	cache = {}
	
	front = North
	length = (size ** 2)
	while len(cache) < length:
		position = (get_pos_x(), get_pos_y())
		
		positions = set()
		if can_move(North):
			positions.add((position[0], position[1] + 1))
		if can_move(East):
			positions.add((position[0] + 1, position[1]))
		if can_move(South):
			positions.add((position[0], position[1] - 1))
		if can_move(West):
			positions.add((position[0] - 1, position[1]))
		
		cache[position] = positions
		
		if can_move(Constants.RIGHT_OF[front]):
			move(Constants.RIGHT_OF[front])
			front = Constants.RIGHT_OF[front]
		elif can_move(front):
			move(front)
		elif can_move(Constants.LEFT_OF[front]):
			move(Constants.LEFT_OF[front])
			front = Constants.LEFT_OF[front]
		else:
			move(Constants.BEHIND_OF[front])
			front = Constants.BEHIND_OF[front]
			
	return cache

#8x8
def function(size):
	def execute(position_start):
		for _ in range(10):
			do_a_flip()
		
		while True:
			Move.to(position_start)
			spawn(size)
			
			front = North
			while get_entity_type() != Entities.Treasure:
				if can_move(Constants.RIGHT_OF[front]):
					move(Constants.RIGHT_OF[front])
					front = Constants.RIGHT_OF[front]
				elif can_move(front):
					move(front)
				elif can_move(Constants.LEFT_OF[front]):
					move(Constants.LEFT_OF[front])
					front = Constants.LEFT_OF[front]
				else:
					move(Constants.BEHIND_OF[front])
					front = Constants.BEHIND_OF[front]
			
			harvest()
	
	return execute

def function_new(size):
	def execute(position_start):
		for _ in range(10):
			do_a_flip()
	
		Move.to(position_start)
		
		spawn(size)
		
		cache = scan(size)
		for i in range(300):
			goal = measure()
			
			position = (get_pos_x(), get_pos_y())
			path = Path.a_star_new(position, goal, cache)
			
			for position in path:
				Move.to(position)
				
				positions = set()
				if can_move(North):
					positions.add((position[0], position[1] + 1))
				if can_move(East):
					positions.add((position[0] + 1, position[1]))
				if can_move(South):
					positions.add((position[0], position[1] - 1))
				if can_move(West):
					positions.add((position[0] - 1, position[1]))
				
				cache[position] = positions
			
				substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
				use_item(Items.Weird_Substance, substance)
			
		goal = measure()
		
		position = (get_pos_x(), get_pos_y())
		path = Path.a_star_new(position, goal, cache)
		
		for position in path:
			Move.to(position)
			
		harvest()
	
	return execute
	
size = 5

positions = []
count = 0
for y in range(6):
	for x in range(6):
		if count >= 32:
			break
		
		position = (x * size + (size // 2), y * size + (size // 2))
		positions.append(position)
		
		count += 1

Utils.initialize()
Bulk.path(positions, function(size))