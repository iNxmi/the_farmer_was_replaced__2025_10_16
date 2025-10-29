def a_speed_1():
	clear()
	cost = get_cost(Unlocks.Speed)[Items.Hay]
	while num_items(Items.Hay) < cost:
		if can_harvest():
			harvest()
			
	unlock(Unlocks.Speed)


def b_expand_1():
	clear()
	cost = get_cost(Unlocks.Expand)[Items.Hay]
	while num_items(Items.Hay) < cost:
		if can_harvest():
			harvest()
			
	unlock(Unlocks.Expand)
	
	
def c_grass_1():
	clear()
	cost = get_cost(Unlocks.Grass)[Items.Hay]
	while num_items(Items.Hay) < cost:
		if can_harvest():
			harvest()
			
		move(North)
		
	unlock(Unlocks.Grass)


def d_plant():
	clear()
	cost = get_cost(Unlocks.Plant)[Items.Hay]
	while num_items(Items.Hay) < cost:
		if can_harvest():
			harvest()
			
		move(North)
		
	unlock(Unlocks.Plant)


def e_speed_2():
	clear()
	cost = get_cost(Unlocks.Speed)[Items.Wood]
	while num_items(Items.Wood) < 20:
		if (get_entity_type() == Entities.Bush) and can_harvest():
			harvest()
			
		plant(Entities.Bush)
			
		move(North)
		
	unlock(Unlocks.Speed)


def f_expand_2():
	clear()
	cost = get_cost(Unlocks.Expand)[Items.Wood]
	while num_items(Items.Wood) < cost:
		if (get_entity_type() == Entities.Bush) and can_harvest():
			harvest()
			
		plant(Entities.Bush)
			
		move(North)
		
	unlock(Unlocks.Expand)


def g_carrots():
	clear()
	cost = get_cost(Unlocks.Carrots)[Items.Wood]
	while num_items(Items.Wood) < cost:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if (get_entity_type() == Entities.Bush) and can_harvest():
					harvest()
					
				plant(Entities.Bush)
					
				move(East)
			move(North)
		
	unlock(Unlocks.Carrots)

def h_expand_3():
	clear()
	cost_wood = get_cost(Unlocks.Expand)[Items.Wood]
	while num_items(Items.Wood) < cost_wood:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if (get_entity_type() == Entities.Bush) and can_harvest():
					harvest()
					
				plant(Entities.Bush)
					
				move(East)
			move(North)
			
	clear()
	cost_carrot = get_cost(Unlocks.Expand)[Items.Carrot]
	while num_items(Items.Carrot) < 20:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if (get_entity_type() == Entities.Carrot) and can_harvest():
					harvest()
					
				plant(Entities.Carrot)
					
				move(East)
			move(North)
		
	unlock(Unlocks.Expand)


def i_speed_3():
	clear()


if __name__ == "__main__":
	a_speed_1()
	b_expand_1()
	c_grass_1()
	d_plant()
	e_speed_2()
	f_expand_2()
	g_carrots()
	h_expand_3()
	i_speed_3()

	while True:
		pass