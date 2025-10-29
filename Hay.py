import Utils, Companion, Move, Path

def simple():
	level_expand = num_unlocked(Unlocks.Expand)
	if level_expand == 0:
		if can_harvest():	
			harvest()
			return
			
	if level_expand == 1:
		if can_harvest():	
			harvest()
		move(North)
		return
	
	for position in Path.snake():
		Move.to(position)
	
		if can_harvest():	
			harvest()
		
def parallel():
	Companion.parallel(Entities.Grass)
	
if __name__ == "__main__":
	Utils.initialize()
	while True:
		parallel()
	