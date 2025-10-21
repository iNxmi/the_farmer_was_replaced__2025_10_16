import Utils, Move, Path, Planter, List, Bulk

planter = Planter.new()
def function_plant(position_start):
	y = position_start[1]
	positions = Path.horizontal(y)
	while len(positions) > 0:
		for position in list(positions):
			Move.to(position)
			
			if (get_entity_type() == Entities.Pumpkin) and can_harvest():
				positions.remove(position)
				continue
				
			planter["set"](Entities.Pumpkin)


def pumpkin():
	Bulk.horizontal(function_plant)
	harvest()


Utils.initialize()
while True:
	pumpkin()
