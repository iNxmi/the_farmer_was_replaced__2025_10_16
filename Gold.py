import Planter, Path, Move, Utils, Constants

planter = Planter.new()

def spawn_maze():
	Utils.initialize()
	planter["set"](Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

while True:
	spawn_maze()
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