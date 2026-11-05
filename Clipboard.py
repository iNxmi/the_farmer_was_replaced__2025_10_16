def execute(position_start):
    y = position_start[1]
    path = Path.horizontal(y)
    
    running = True
    while running:
        running = False
        for position in path:
            Move.to(position)
            
            if get_ground_type() != Grounds.Basalt:
                dig()
                running = True
    
Bulk.horizontal(execute)