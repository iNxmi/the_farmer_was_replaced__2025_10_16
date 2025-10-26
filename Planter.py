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
	
	minimum_water = 0.0
	def get_minimum_water():
		global minimum_water
		return minimum_water
	def set_minimum_water(value):
		global minimum_water
		minimum_water = value
		
	forcing = False
	def get_forcing():
		global forcing
		return forcing
	def set_forcing(value):
		global forcing
		forcing = value
	
	def set(entity):
		if get_forcing() or (get_entity_type() != entity) or (get_harvesting() and can_harvest()):
			cost = get_cost(entity)
			for item in cost:
				needed = cost[item]
				actual = num_items(item)
				if actual < needed:
					log["warning"]("Nor enough '" + str(item) + "', needed=" + str(needed) + " actual=" + str(actual))
					return
					
		if (get_harvesting() and can_harvest()) or get_forcing():
			harvest()

		while get_tilling() and get_ground_type() != Constants.ENTITY_TO_GROUND[entity]:
			till()
			
		while (get_water() < get_minimum_water()) and num_items(Items.Water) >= 1:
			use_item(Items.Water)
		
		if get_entity_type() != entity:
			plant(entity)
	
	return {
		"get_harvesting": get_harvesting,
		"set_harvesting": set_harvesting,
		
		"get_tilling": get_tilling,
		"set_tilling": set_tilling,
		
		"get_minimum_water": get_minimum_water,
		"set_minimum_water": set_minimum_water,
		
		"get_forcing": get_forcing,
		"set_forcing": set_forcing,
	
		"set": set
	}