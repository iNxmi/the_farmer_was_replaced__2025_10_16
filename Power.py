import Bulk, Planter, Path, Utils, Move

if __name__ == "__main__":
    planter = Planter.new()
    planter["set_forcing"](False)
    planter["set_harvesting"](False)
    #planter["set_minimum_water"](0.9)
    
    def plant(position_start):
        y = position_start[1]
        path = Path.horizontal(y)
    
        for position in path:
            Move.to(position)
            planter["set"](Entities.Sunflower)
        
    def collect(position_start, level):
        y = position_start[1]
        path = Path.horizontal(y)
    
        for position in path:
            Move.to(position)
            
            if measure() != level:
                continue
            
            while not can_harvest():
                pass
                
            harvest()
    
    Utils.initialize()
    Bulk.horizontal(plant)
    
    for level in range(15, 6, -1):
        
        def function(position_start):
            collect(position_start, level)
        
        Bulk.horizontal(function)

def old():
    planter = Planter.new()
    planter["set_forcing"](False)
    planter["set_harvesting"](True)
    planter["set_minimum_water"](0.9)
    
    def plant(position_start):
        y = position_start[1]
        path = Path.horizontal(y)
        
        levels = dict()
    
        for position in path:
            Move.to(position)
            planter["set"](Entities.Sunflower)
            levels[position] = measure()
        
        return levels
    
    Utils.initialize()
    
    levels = dict()
    for level in range(7, 16):
        levels[level] = set()
        
    result = Bulk.horizontal(plant)
    for dict in result:
        for position in dict:
            level = dict[position]
            levels[level].add(position)
    
    quick_print(levels)