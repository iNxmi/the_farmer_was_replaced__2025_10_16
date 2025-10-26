import Utils, Companion, Planter, Path, Move

def simple():
	path = Path.snake()
	planter = Planter.new()
	for position in path:
		if not function_condition():
			break
			
		Move.to(position)
		
		if can_harvest():
			harvest()
			
		planter["set"](Entities.Carrot)
			

def parallel():
	Companion.parallel(Entities.Carrot)
	
if __name__ == "__main__":
	Utils.initialize()
	while True:
		parallel()
	