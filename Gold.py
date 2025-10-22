import Planter, Path, Move, Utils, Constants, Logger

log = Logger.new("Gold")
planter = Planter.new()

def spawn_maze():
	Utils.initialize()
	planter["set"](Entities.Bush)
	substance = get_world_size() * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	use_item(Items.Weird_Substance, substance)

def scan():
	cache = {}
	
	front = North
	length = (get_world_size() ** 2)
	while len(cache) < length:
		
		log["debug"](str(len(cache)) + "/" + str(length))
		
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

spawn_maze()
cache = scan()
iteration = 0
while True:
	gold = (get_world_size() ** 2) * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	gold_mul = gold * (iteration + 1)
	
	log["debug"]("Iteration=" + str(iteration) + " Gold=" + str(gold_mul))

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
	
	if gold_mul < 2000000:
		substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)
	else:
		harvest()
		break
		
	iteration += 1
	
