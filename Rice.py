import Utils, Path, Move, Bulk

def parallel():
    
    def execute(position_start):
        y = position_start[1]
        path = Path.horizontal(y)
        
        planted = False

        for position in path:
            Move.to(position)
            
            if get_ground_type() == Grounds.Clay:
                plant(Entities.Rice)
                planted = True
            else:
                dig()
                
        if not planted:
            return
        
        for position in path:
            Move.to(position)
            
            if get_entity_type() != Entities.Rice:
                continue
            
            while not can_harvest():
                do_a_flip()
                        
            harvest()
            dig()
    
    Bulk.horizontal(execute)
    
if __name__ == "__main__":
    Utils.initialize()
    
    jump(Unlocks.Rice)
    
    while True:
        parallel()