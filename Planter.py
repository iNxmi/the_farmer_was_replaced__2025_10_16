import Constants, Logger

log = Logger.new("Planter")

def new():
	
	harvesting = False
	def get_harvesting():
		global harvesting
		return harvesting
	def set_harvesting(value):
		global harvesting
		harvesting = value
		
	tilling = True
	def get_tilling():
		global tilling
		return tilling
	def set_tilling(value):
		global tilling
		tilling = value
	
	watering_threshold = 0.0
	def get_watering_threshold():
		global watering_threshold
		return watering_threshold
	def set_watering_threshold(value):
		global watering_threshold
		watering_threshold = value
	
	fertilizing = False
	def get_fertilizing():
		global fertilizing
		return fertilizing
	def set_fertilizing(value):
		global fertilizing
		fertilizing = value
		
	forcing = False
	def get_forcing():
		global forcing
		return forcing
	def set_forcing(value):
		global forcing
		forcing = value
	
	def set(entity):
		cost = get_cost(entity)
		for item in cost:
			needed = cost[item]
			actual = num_items(item)
			if actual < needed:
				log["warn"]("Nor enough '" + str(item) + "', needed=" + str(needed) + " actual=" + str(actual))
			
		if (get_harvesting() and can_harvest()) or get_forcing():
			harvest()

		while get_tilling() and get_ground_type() != Constants.ENTITY_TO_GROUND[entity]:
			till()
			
		while get_water() <= get_watering_threshold():
			use_item(Items.Water)
		
		if get_entity_type() != entity:
			plant(entity)
		
		if get_fertilizing():
			use_item(Items.Fertilizer)
	
	return {
		"get_harvesting": get_harvesting,
		"set_harvesting": set_harvesting,
		
		"get_tilling": get_tilling,
		"set_tilling": set_tilling,
		
		"get_watering_threshold": get_watering_threshold,
		"set_watering_threshold": set_watering_threshold,
		
		"get_fertilizing": get_fertilizing,
		"set_fertilizing": set_fertilizing,
		
		"get_forcing": get_forcing,
		"set_forcing": set_forcing,
	
		"set": set
	}