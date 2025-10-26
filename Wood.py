import Utils, Companion, Planter, Path, Move

def simple():
	path = Path.snake()
	planter = Planter.new()
	for position in path:
		Move.to(position)
		
		if can_harvest():
			harvest()
			
		if (position[0] + position[1]) % 2 == 0:
			planter["set"](Entities.Bush)
		else:
			planter["set"](Entities.Tree)

def parallel():
	Companion.parallel(Entities.Tree)
	
if __name__ == "__main__":
	Utils.initialize()
	while True:
		parallel()
	