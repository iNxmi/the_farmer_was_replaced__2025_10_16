import Move, Path, Math
import Hay, Cactus

def hay(add):
	clear()
	
	level_expand = num_unlocked(Unlocks.Expand)
	count_start = num_items(Items.Hay)
	count_goal = count_start + add
	while num_items(Items.Hay) < count_goal:
		if num_unlocked(Unlocks.Megafarm) <= 0:
			Hay.simple()
		else:
			Hay.parallel()
	
def wood(add):
	clear()

	count_start = num_items(Items.Wood)
	count_goal = count_start + add
	while num_items(Items.Wood) < count_goal:
		for position in Path.snake():
			Move.to(position)
		
			if (get_entity_type() == Entities.Bush or get_entity_type() == Entities.Tree) and can_harvest():	
				harvest()
			
			if num_unlocked(Unlocks.Trees) <= 0:
				if get_entity_type() != Entities.Bush:
					plant(Entities.Bush)
			else:
				if (get_pos_x() + get_pos_y()) % 2 == 1:
					if get_entity_type() != Entities.Bush:
						plant(Entities.Bush)
				else:
					if get_entity_type() != Entities.Tree:
						plant(Entities.Tree)
	
def carrot(add):
	farm_cost(Entities.Carrot, add, 1.1)
	
	clear()
	
	count_start = num_items(Items.Carrot)
	count_goal = count_start + add
	while num_items(Items.Carrot) < count_goal:
		for position in Path.snake():
			Move.to(position)
			
			if get_entity_type() == Entities.Carrot and can_harvest():	
				harvest()

			if get_ground_type() != Grounds.Soil:
				till()
			
			if get_entity_type() != Entities.Carrot:
				plant(Entities.Carrot)

def pumpkin(add):
	farm_cost(Entities.Pumpkin, add, 1.25)
	
	clear()
	count_start = num_items(Items.Pumpkin)
	count_goal = count_start + add
	while num_items(Items.Pumpkin) < count_goal:
		positions = Path.snake()
		while len(positions) > 0:
			for position in list(positions):
				Move.to(position)	
			
				if (get_entity_type() == Entities.Pumpkin) and can_harvest():
					positions.remove(position)
					continue
					
				if get_entity_type() != Entities.Pumpkin:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Pumpkin)
			
		harvest()
		
def cactus(add):
	farm_cost(Entities.Cactus, add, 1.1)
	
	clear()
	count_start = num_items(Items.Cactus)
	count_goal = count_start + add
	while num_items(Items.Cactus) < count_goal:
		Cactus.simple()

ITEM_TO_FUNCTION = {
	Items.Hay: hay,
	Items.Wood: wood,
	Items.Carrot: carrot,
	Items.Pumpkin: pumpkin,
	Items.Cactus: cactus
}

def farm_cost(object, amount = 1, multiplier = 1):
	cost = get_cost(object)
	for item in cost:
		value = cost[item] * amount
		iterations = Math.ceil(value / (get_world_size() ** 2))
		count = iterations * (get_world_size() ** 2) * multiplier
		
		function = ITEM_TO_FUNCTION[item]
		function(count)

def auto_unlock(ul):
	farm_cost(ul)
	
	success = unlock(ul)
	tuple = (ul, success, num_unlocked(ul))
	quick_print(tuple)

if __name__ == "__main__":
	auto_unlock(Unlocks.Speed)
	auto_unlock(Unlocks.Expand)
	auto_unlock(Unlocks.Plant)
	auto_unlock(Unlocks.Speed)
	auto_unlock(Unlocks.Expand)

	auto_unlock(Unlocks.Grass)
	auto_unlock(Unlocks.Carrots)
	auto_unlock(Unlocks.Trees)
	auto_unlock(Unlocks.Speed)
	auto_unlock(Unlocks.Expand)
	auto_unlock(Unlocks.Speed)
	auto_unlock(Unlocks.Expand)
	auto_unlock(Unlocks.Speed)
	
	auto_unlock(Unlocks.Trees)
	auto_unlock(Unlocks.Watering)
	auto_unlock(Unlocks.Fertilizer)
	auto_unlock(Unlocks.Pumpkins)
	auto_unlock(Unlocks.Pumpkins)
	auto_unlock(Unlocks.Grass)
	auto_unlock(Unlocks.Carrots)
	auto_unlock(Unlocks.Grass)
	auto_unlock(Unlocks.Trees)
	auto_unlock(Unlocks.Trees)
	auto_unlock(Unlocks.Carrots)
	auto_unlock(Unlocks.Grass)
	auto_unlock(Unlocks.Expand)
	auto_unlock(Unlocks.Carrots)
	#auto_unlock(Unlocks.Expand)
	auto_unlock(Unlocks.Cactus)
	auto_unlock(Unlocks.Trees)
	auto_unlock(Unlocks.Dinosaurs)

	while True:
		pass