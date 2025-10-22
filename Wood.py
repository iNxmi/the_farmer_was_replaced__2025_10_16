import Utils, Path, Companion, Planter

planter = Planter.new()
planter["set_watering_threshold"](0.75)

while True:
	Utils.initialize(31)
	Companion.full(Entities.Tree, planter)