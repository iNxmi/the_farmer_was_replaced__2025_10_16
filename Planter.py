import Constants

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
	
	def set(entity):
		global harvesting
		if harvesting and can_harvest():
			harvest()

		global tilling
		while tilling and get_ground_type() != Constants.ENTITY_TO_GROUND[entity]:
			till()
			
		global watering_threshold
		while get_water() < watering_threshold:
			use_item(Items.Water)
				
		if get_entity_type() != entity:
			plant(entity)
		
		global fertilizing
		if fertilizing:
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
	
		"set": set
	}