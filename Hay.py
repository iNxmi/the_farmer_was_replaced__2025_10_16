import Utils, Companion, Move, Path

def simple():
	path = Path.snake()
	for position in path:
		Move.to(position)
		
		if can_harvest():
			harvest()
		
def parallel():
	Companion.parallel(Entities.Grass)
	
if __name__ == "__main__":
	Utils.initialize()
	while True:
		parallel()
	