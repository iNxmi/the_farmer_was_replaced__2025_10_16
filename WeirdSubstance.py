import Plant, Path, Move, Utils


def weird_substance(path):
	for position in path:
		Move.to(position)
		Plant.set(Entities.Grass)
		use_item(Items.Fertilizer)
		harvest()


Utils.initialize()
path = Path.snake()
while True:
	weird_substance(path)