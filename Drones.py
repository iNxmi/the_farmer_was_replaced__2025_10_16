def join(lst):
	drones = list(lst)
	while len(drones) > 0:
		for drone in drones:
			if has_finished(drone):
				drones.remove(drone)
	