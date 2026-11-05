import Utils, Move, Path, Bulk

Utils.initialize()

GROUNDS = {Grounds.Dirt, Grounds.Dry_Rice_Terrace, Grounds.Clay}
def execute(position_start):
    y = position_start[1]
    path = Path.horizontal(y)
    
    done = False
    while not done:
        done = True
        for position in path:
            Move.to(position)
            
            ground = get_ground_type()
            if ground == Grounds.Clay:
                pass
            
            if get_ground_type() not in GROUNDS:
                continue
            
            if can_harvest():
                harvest()
            elif get_ground_type() in GROUNDS:
                dig()
                done = False
            
            plant(Entities.Rice)

jump(Unlocks.Rice)
while True:
    Bulk.horizontal(execute)