import Utils, Path, Companion

planter = Planter.new()
planter["set_watering_threshold"](0.75)

while True:
	Utils.initialize()
	Companion.full(Entities.Carrot, planter)